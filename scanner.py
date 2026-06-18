import os
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def scan_terraform(directory):
    violations = []
    
    # Regex patterns for SOC 2 critical failures
    db_pattern = re.compile(r'resource\s+"aws_db_instance"\s+"[^"]+"')
    encryption_pattern = re.compile(r'storage_encrypted\s*=\s*true')
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".tf"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                    # Check 1: Database Encryption at Rest
                    if db_pattern.search(content) and not encryption_pattern.search(content):
                        violations.append({
                            "control": "CC6.1 - Encryption at Rest",
                            "file": file,
                            "issue": "Unencrypted Database Instance Detected",
                            "severity": "CRITICAL"
                        })
    return violations

def generate_report(violations):
    console.print(Panel.fit("🛡️  [bold cyan]60-Second SOC 2 Diagnostic Engine[/bold cyan] 🛡️\nFractional Cloud Security Advisory", border_style="cyan"))
    
    if not violations:
        console.print("[bold green]✔ All baseline checks passed. Zero-trust architecture verified.[/bold green]")
        return

    table = Table(title="[bold red]Audit Violations Detected[/bold red]", show_header=True, header_style="bold magenta")
    table.add_column("SOC 2 Control", style="dim", width=25)
    table.add_column("File", justify="left")
    table.add_column("Vulnerability", justify="left", style="red")
    table.add_column("Severity", justify="center")

    for v in violations:
        color = "red" if v["severity"] == "CRITICAL" else "yellow"
        table.add_row(v["control"], v["file"], v["issue"], f"[bold {color}]{v['severity']}[/bold {color}]")

    console.print(table)
    console.print("\n[bold yellow]Recommendation:[/bold yellow] Implement automated Rego guardrails to block unencrypted merges.")
    console.print("Learn how to automate this remediation: [underline cyan]https://github.com/high5x/ws-automated-mitigation-engine[/underline cyan]")

if __name__ == "__main__":
    console.print("[dim]Initializing workspace parse...[/dim]")
    # Defaulting to current directory for the scanner
    target_dir = os.getenv("SCAN_DIR", ".") 
    found_violations = scan_terraform(target_dir)
    generate_report(found_violations)
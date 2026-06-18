# 🛡️ 60-Second SOC 2 Readiness Scanner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Security: Guardrails](https://img.shields.io/badge/Security-Guardrails--as--Code-red.svg)]()

A lightweight, zero-dependency, read-only static analysis tool engineered to diagnose critical cloud infrastructure configuration gaps before auditors do. Stop letting security compliance bottlenecks stall your enterprise procurement pipelines.

Developed to help rapid-growth engineering teams evaluate their zero-trust perimeters and technical control baselines in under 60 seconds.

---

## ⚡ The Problem

Series A and B startups routinely lose or delay lucrative enterprise deals because their cloud environments fail baseline security reviews. Manually combing through infrastructure-as-code files to verify posture is slow, prone to human error, and pulls core engineers away from shipping product.

This diagnostic engine provides instant, objective visibility into configuration violations (such as TSC CC6.1 encryption requirements) across your local engineering workspaces.

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your workstation.

### 2. Installation
Clone the repository and install the high-fidelity terminal user interface dependency:

```bash
git clone [https://github.com/high5x/soc2-readiness-scanner.git](https://github.com/high5x/soc2-readiness-scanner.git)
cd soc2-readiness-scanner
pip install -r requirements.txt
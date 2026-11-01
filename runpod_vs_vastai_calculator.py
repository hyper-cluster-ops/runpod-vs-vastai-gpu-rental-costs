#!/usr/bin/env python3
"""
RunPod vs Vast.ai GPU Cloud Rental Cost Comparison Calculator 2026.
Compares monthly and annual infrastructure expenses between community and marketplace GPU providers.
"""
import argparse

def compare_costs(hours, runpod_rate, vastai_rate):
    runpod_monthly = hours * runpod_rate
    vastai_monthly = hours * vastai_rate
    monthly_diff = runpod_monthly - vastai_monthly
    annual_runpod = runpod_monthly * 12.0
    annual_vastai = vastai_monthly * 12.0
    annual_diff = monthly_diff * 12.0
    return {
        "runpod_monthly": runpod_monthly,
        "vastai_monthly": vastai_monthly,
        "monthly_diff": monthly_diff,
        "annual_runpod": annual_runpod,
        "annual_vastai": annual_vastai,
        "annual_diff": annual_diff
    }

def main():
    parser = argparse.ArgumentParser(description="RunPod vs Vast.ai GPU Cost Comparison")
    parser.add_argument("--hours", type=float, default=300.0, help="Monthly compute hours (default: 300)")
    parser.add_argument("--runpod-rate", type=float, default=0.74, help="RunPod hourly rate in USD (default: $0.74 for RTX 4090)")
    parser.add_argument("--vastai-rate", type=float, default=0.35, help="Vast.ai hourly rate in USD (default: $0.35 for RTX 4090)")
    args = parser.parse_args()

    res = compare_costs(args.hours, args.runpod_rate, args.vastai_rate)
    print(f"RunPod Monthly (@${args.runpod_rate:.2f}/hr):  ${res['runpod_monthly']:.2f}")
    print(f"Vast.ai Monthly (@${args.vastai_rate:.2f}/hr): ${res['vastai_monthly']:.2f}")
    print(f"Monthly Cost Difference:     ${res['monthly_diff']:.2f}")
    print(f"Annual RunPod Expense:       ${res['annual_runpod']:.2f}")
    print(f"Annual Vast.ai Expense:      ${res['annual_vastai']:.2f}")
    print(f"Annual Projected Savings:    ${res['annual_diff']:.2f}")

if __name__ == "__main__":
    main()

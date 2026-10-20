#!/usr/bin/env python3
"""
SelfHostSwitch — Zapier & Make vs. Self-Hosted n8n & Cloud Scraper Cost Calculator — Command-Line Cost Calculator
Live Web Calculator: https://sectoroneventures.github.io/selfhost-switch/
"""
import argparse

PROVIDERS = [
  {
    "name": "Self-Hosted n8n + Apify Worker Stack",
    "cost_per_unit": 0.12,
    "min_monthly": 9.0,
    "speed_note": "Unlimited internal workflow steps + $5/mo free Apify credit",
    "cta_label": "Get n8n Production Setup Guide \u2192",
    "cta_url": "https://www.checkout-ds24.com/redir/667670/infrabench7552/",
    "highlight": true
  },
  {
    "name": "n8n + ScrapingBee Stealth Proxy API",
    "cost_per_unit": 0.18,
    "min_monthly": 12.0,
    "speed_note": "Best for HTTP scraping workflows behind Cloudflare",
    "cta_label": "Try ScrapingBee (1,000 Free Calls) \u2192",
    "cta_url": "https://www.scrapingbee.com?fpr=infrabench7552",
    "highlight": false
  },
  {
    "name": "Per-Task Cloud Automation SaaS (Standard Tier)",
    "cost_per_unit": 2.4,
    "min_monthly": 49.0,
    "speed_note": "Charges for every filter, loop, and webhook step",
    "cta_label": "Switch to Self-Hosted Stack \u2192",
    "cta_url": "https://apify.com?fpr=infrabench7552",
    "highlight": false
  }
]

def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate how much you save switching high-volume webhook and scraping workflows from per-task SaaS plans to self-hosted n8n + Apify/ScrapingBee.")
    parser.add_argument("--volume", type=float, default=150, help="Monthly Workflow Tasks & Web Scraping Actions (in Thousands)")
    args = parser.parse_args()
    print(f"=== {args.volume:g} k tasks/mo Cost Comparison ===")
    for p in PROVIDERS:
        cost = max(float(p["min_monthly"]), args.volume * float(p["cost_per_unit"]))
        print(f"* {p['name']}: ${cost:,.2f}/mo ({p['speed_note']})")
        print(f"  -> {p['cta_url']}")
    print(f"\nInteractive web calculator: https://sectoroneventures.github.io/selfhost-switch/")

if __name__ == "__main__":
    main()

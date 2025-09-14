#!/usr/bin/env python3
"""
Scripts for running tests and demos
"""

import subprocess
import sys
from app.models.stock import Stock


def run_tests():
    """Run all tests"""
    result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], cwd=".")
    return result.returncode


def run_stock_tests():
    """Run stock tests with output"""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_stock.py", "-v", "-s"], cwd="."
    )
    return result.returncode


def run_player_tests():
    """Run player tests"""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_player.py", "-v", "-s"], cwd="."
    )
    return result.returncode


def demo_stock():
    """Demo stock price changes"""
    print("=== Stock Price Demo ===")
    s = Stock("Tesla", "TSLA", 100.0, 1000)
    print(f"Initial: {s}")

    print(f"After buying 10 shares: {s.buy(10):.2f}")
    print(f"After buying 50 shares: {s.buy(50):.2f}")
    print(f"After buying 100 shares: {s.buy(100):.2f}")

    print(f"Final: {s}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "test":
            sys.exit(run_tests())
        elif command == "test-stock":
            sys.exit(run_stock_tests())
        elif command == "test-player":
            sys.exit(run_player_tests())
        elif command == "demo":
            sys.exit(demo_stock())
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    else:
        print("Available commands: test, test-stock, test-player, demo")
        sys.exit(1)

#!/usr/bin/env python3
"""
Demo: Minervini Stock Analyzer
=============================

This demo script showcases the Minervini Stock Buying Checklist analyzer
with popular stocks to demonstrate how it works.

Educational Example: Analyze multiple stocks and compare results
"""

from minervini_stock_analyzer import MinerviniAnalyzer
import matplotlib.pyplot as plt
from datetime import datetime
import os

def demo_analysis():
    """Demo function to analyze multiple stocks"""
    
    # Sample stocks to analyze (mix of strong and weak candidates)
    demo_stocks = ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'TSLA']
    
    print("🚀 MINERVINI STOCK ANALYZER DEMO")
    print("=" * 50)
    print("Analyzing sample stocks using Mark Minervini's criteria...")
    print("This may take a moment to fetch real-time data...\n")
    
    results = []
    
    for stock in demo_stocks:
        print(f"🔍 Analyzing {stock}...")
        analyzer = MinerviniAnalyzer(stock)
        
        try:
            result = analyzer.analyze_stock()
            if result:
                results.append(result)
                
                # Create chart (suppress display for demo)
                plt.ioff()  # Turn off interactive mode
                analyzer.create_chart(f"{stock}_analysis_chart.png")
                plt.close('all')  # Close all figures
                
        except Exception as e:
            print(f"❌ Error analyzing {stock}: {e}")
        
        print("\n" + "="*60 + "\n")
    
    # Summary Report
    print("📊 DEMO ANALYSIS SUMMARY")
    print("=" * 30)
    
    buy_candidates = []
    avoid_stocks = []
    
    for result in results:
        if result['recommendation'] == 'BUY':
            buy_candidates.append(result)
        else:
            avoid_stocks.append(result)
    
    print(f"\n🟢 BUY CANDIDATES ({len(buy_candidates)}):")
    for stock in buy_candidates:
        print(f"  • {stock['symbol']}: ${stock['current_price']:.2f} "
              f"(Risk: {stock['risk_percent']:.1f}%, Stop: ${stock['stop_loss']:.2f})")
    
    print(f"\n🔴 AVOID/HOLD ({len(avoid_stocks)}):")
    for stock in avoid_stocks:
        print(f"  • {stock['symbol']}: ${stock['current_price']:.2f} "
              f"(Phase 1: {stock['phase1_score']}, Phase 2: {stock['phase2_score']})")
    
    print(f"\n📈 CHARTS GENERATED:")
    for result in results:
        chart_file = f"{result['symbol']}_analysis_chart.png"
        if os.path.exists(chart_file):
            print(f"  • {chart_file}")
    
    # Create summary report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_file = f"minervini_demo_summary_{timestamp}.txt"
    
    with open(summary_file, 'w') as f:
        f.write("MINERVINI STOCK ANALYZER - DEMO SUMMARY\n")
        f.write("=" * 45 + "\n")
        f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write(f"BUY CANDIDATES ({len(buy_candidates)}):\n")
        for stock in buy_candidates:
            f.write(f"  {stock['symbol']}: ${stock['current_price']:.2f} "
                   f"(Risk: {stock['risk_percent']:.1f}%, Stop: ${stock['stop_loss']:.2f})\n")
        
        f.write(f"\nAVOID/HOLD ({len(avoid_stocks)}):\n")
        for stock in avoid_stocks:
            f.write(f"  {stock['symbol']}: ${stock['current_price']:.2f} "
                   f"(Phase 1: {stock['phase1_score']}, Phase 2: {stock['phase2_score']})\n")
        
        f.write(f"\nDETAILED RESULTS:\n")
        f.write("-" * 20 + "\n")
        for result in results:
            f.write(f"\n{result['symbol']}:\n")
            f.write(f"  Recommendation: {result['recommendation']}\n")
            f.write(f"  Phase 1 Score: {result['phase1_score']}\n")
            f.write(f"  Phase 2 Score: {result['phase2_score']}\n")
            f.write(f"  Entry Signal: {result['entry_signal']}\n")
            f.write(f"  Current Price: ${result['current_price']:.2f}\n")
            f.write(f"  Stop Loss: ${result['stop_loss']:.2f}\n")
            f.write(f"  Risk %: {result['risk_percent']:.1f}%\n")
    
    print(f"\n📄 Summary report saved to: {summary_file}")
    
    return results

def analyze_single_stock(symbol):
    """Analyze a single stock interactively"""
    print(f"\n🎯 SINGLE STOCK ANALYSIS: {symbol.upper()}")
    print("=" * 40)
    
    analyzer = MinerviniAnalyzer(symbol)
    result = analyzer.analyze_stock()
    
    if result:
        # Generate chart
        analyzer.create_chart()
        print(f"\n✅ Analysis complete for {symbol.upper()}")
        return result
    else:
        print(f"❌ Failed to analyze {symbol.upper()}")
        return None

def educational_explanation():
    """Print educational explanation of Minervini's method"""
    explanation = """
📚 MINERVINI'S STOCK BUYING CHECKLIST EXPLAINED
==============================================

Mark Minervini's method focuses on identifying stocks in strong uptrends 
with proper base formations before breakouts. Here's what this analyzer checks:

PHASE 1: TREND TEMPLATE ✅
• Price above 50, 150, 200-day moving averages
• Moving averages in proper order (50>150>200)  
• Price at least 30% above 52-week low
• Price within 25% of 52-week high
• Price above 10 & 21-day EMAs

PHASE 2: VCP BASE FORMATION 📈
• Series of contractions getting smaller over time
• Volume declining during pullbacks (dry up)
• Price tightening in recent bars
• Proper base structure before breakout

ENTRY TRIGGER 🚀
• Breakout above resistance on volume surge
• Volume 50%+ above average on breakout
• Clear pivot point with conviction

RISK MANAGEMENT 💰
• Stop loss below recent support
• Risk 1-2% of portfolio per trade
• Position sizing based on stop distance

This systematic approach helps identify stocks with the highest probability
of significant moves while managing downside risk effectively.
"""
    print(explanation)

def main():
    """Main demo function"""
    print("Welcome to the Minervini Stock Analyzer Demo!")
    print("\nChoose an option:")
    print("1. Run demo analysis on sample stocks")
    print("2. Analyze a specific stock")
    print("3. Show educational explanation")
    print("4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                demo_analysis()
                break
            elif choice == '2':
                symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
                if symbol:
                    analyze_single_stock(symbol)
                break
            elif choice == '3':
                educational_explanation()
                break
            elif choice == '4':
                print("Thanks for using the Minervini Stock Analyzer!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
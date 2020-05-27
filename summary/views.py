from django.shortcuts import render

# Create your views here.
from summary.models import Stock, StockInstance, PreviousClose, OpenPrice, EnterpriseValue, MarketCap, EarningsPerShare, PriceToEarnings
from django.views import generic


# class IndexView(generic.ListView):
#     template_name = 'summary/index.html'
#     context_object_name = 'most_growing_stock'

#     # Generate counts of some of the main objects
#     num_books = Stock.objects.all().count()
#     num_instances = StockInstance.objects.all().count()
#     num_market_cap = MarketCap.objects.filter(market_cap__gt=1000000000).count()

#     def get_queryset(self):
#         """
#         Return the best ten stocks based on their PriceToEarnings ratio.
#         """
#         # return Question.objects.order_by('-pub_date')[:5]
#         return Stock.objects.filter(
#             pe_ratio__lte=20
#         ).order_by('-pe_ratio')[:10]

# IndexView reformulated
# View (class-based)
class StockListView(generic.ListView):
    model = Stock

    context_object_name = 'stock_list'   # your own name for the list as a template variable
    queryset = Stock.objects.filter(stock_description__icontains='Artificial Intelligence')[:5] # Get 5 stocks containing in their descriiption the word "Artificial Intelligence"
    template_name = 'summary/stock_list.html'  # Specify your own template name/location

class StockDetailView(generic.DetailView):
    model = Stock
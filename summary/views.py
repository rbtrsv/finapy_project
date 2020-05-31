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
    paginate_by = 10

from django.contrib.auth.mixins import LoginRequiredMixin

class OwnedStocksByClientListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing stocks owned by the current user."""
    model = StockInstance
    template_name = 'summary/stockinstance_list_owned_client.html'

    def get_queryset(self):
        return StockInstance.objects.filter(client=self.request.user).filter(status__exact='o')

import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# from summary.forms import StockHaltForm

# @permission_required('catalog_app.can_mark_returned')
# def renew_book_librarian(request, pk):
#     """View function for renewing a specific BookInstance by librarian."""
#     book_instance = get_object_or_404(BookInstance, pk=pk)

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':

#         # Create a form instance and populate it with data from the request (binding):
#         form = RenewBookForm(request.POST)

#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             book_instance.due_back = form.cleaned_data['renewal_date']
#             book_instance.save()

#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('all-borrowed'))

#     # If this is a GET (or any other method) create the default form.
#     else:
#         proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

#     context = {
#         'form': form,
#         'book_instance': book_instance,
#     }

#     return render(request, 'catalog_app/book_renew_librarian.html', context)

# To amend:
# @permission_required('summary.can_mark_trading_halt')
# def halt(request, stock_id):
#     stock_instance = get_object_or_404(Stock, pk=stock_id)

#     if request.method == 'POST':
#         form = TradingHaltForm(request.POST)

#         if form.is_valid():
#             stock_instance.stock_halt = True
#             stock_instance.save()

#         return HttpResponseRedirect('all-halted')
    
#     else:
#         pass

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

class StockCreate(CreateView):
    model = Stock
    fields = '__all__'
    initial = {'price_date': timezone.now()}

class StockUpdate(UpdateView):
    model = Stock
    fields = ['stock_name', 'stock_ticker', 'stock_description', 'open_price']

class StockDelete(DeleteView):
    model = Stock
    success_url = reverse_lazy('authors')
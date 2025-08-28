from django.shortcuts import render, get_object_or_404, redirect
from .models import Pool
from .forms import CommentForm

def pool_list(request):
    pools = Pool.objects.all()
    return render(request, 'pools/pool_list.html', {'pools': pools})

def pool_detail(request, pk):
    pool = get_object_or_404(Pool, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pool = pool
            comment.save()
            return redirect('pools:pool_detail', pk=pool.pk)
    else:
        form = CommentForm()
    return render(request, 'pools/pool_detail.html', {'pool': pool, 'form': form})

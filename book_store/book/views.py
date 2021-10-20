from django.shortcuts import render,get_object_or_404,redirect
from book.models import Category,Book,Subcategory, Images, Rating
from django.contrib import messages
from django.contrib.auth import login, logout
from book.forms import UserRegisterForm, UserLoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from comment.models import Comment
from comment.forms import CommentForm
from order.models import ShopCart


def base(request):
    category = Category.objects.all()
    catdata = Subcategory.objects.all()
    books = Book.objects.order_by('?')[:12]
    book_circle = Book.objects.order_by('?')[:6]

    stock = Book.objects.order_by('-create_at').first()

    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity


    contact = {'category': category,
               'books': books,
               'book_circle': book_circle,
               'stock': stock,
               'catdata': catdata,
                'shopcart': shopcart,
               'total': total,
               }

    return render(request, 'base.html', contact)


def get_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        book_search = Book.objects.filter(title__contains=searched)


        return render(request, 'search.html', {'searched': searched, 'book_search': book_search})
    else:

        return render(request, 'search.html')



def get_single(request, slug: int):
    review = Rating.objects.filter(id=slug)
    book_single = get_object_or_404(Book, id=slug)
    category = Category.objects.all()
    images = Images.objects.filter(product_id=slug)
    books_single = Book.objects.order_by('?')[:4]
    book_circle_single = Book.objects.order_by('?')[:4]

    comments = Comment.objects.filter(post=book_single)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = book_single
            comment.save()
            return HttpResponseRedirect(reverse('single', args=[slug]))
    else:
        form = CommentForm()

    ratings = Rating.objects.filter(post=book_single, score=0).order_by("?").first()


    context = {
        "book_single": book_single,
        'category': category,
        'books_single': books_single,
        'book_circle_single': book_circle_single,
        'images': images,
        'comments': comments,
        'form': form,
        'ratings': ratings,
        'review': review
    }
    return render(request, "single.html", context)





def get_category(request, category_id):
    book = Book.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    catdata = Category.objects.get(pk=category_id)
    catdatas = Subcategory.objects.all()
    context = {
        'book': book,
        'categories': categories,
        'category': category,
        'catdata': catdata,
        'catdatas': catdatas
    }
    return render(request, 'category.html', context)




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('base')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
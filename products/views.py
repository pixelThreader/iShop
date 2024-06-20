from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import (
    Category,
    AllProducts,
    Flavour,
    ProductComment,
    CommentLike,
    CommentDislike,
)
from cart.models import Cart
import random
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def category(request):
    allCategory = Category.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    context = {"allCategory": allCategory, "NoCartItems": cart_items}
    return render(request, "products/categories.html", context)


def products(request):
    allProduct = AllProducts.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    NoCardData = AllProducts.objects.all().count()
    data_per_page = 5
    paginator = Paginator(allProduct, data_per_page)
    page_no = request.GET.get("page")
    serviceData = paginator.get_page(page_no)
    context = {
        "allProduct": serviceData,
        "NoCartItems": cart_items,
        "data": serviceData,
        "total_data": NoCardData,
        "DataPerPage": data_per_page,
    }
    return render(request, "products/allProducts.html", context)


def uploadProduct(request):

    # Generating Random Ids
    def GenerateRandomId(Name, InputLength):
        N = int(InputLength)
        alpha = "!@$%&?^⨏⨒⨝⫰⫯ɐÆʘʭ⁕⁑⁋⁊"
        numerics = "1234567890"
        res = "".join(random.choices(alpha + numerics, k=N))
        generatedid = Name[:1] + "iS91" + res
        return generatedid

    if request.method == "POST":
        iceCreamName = request.POST.get("icecreamName")
        iceCreamSlug = slugify(iceCreamName)
        iceCreamImage = request.FILES.get("IceCreamPhoto")
        icecreamManufacture = request.POST.get("IceCreamMaker")
        iCAt = request.POST.get("iceCreamCategory")
        iceCreamCategory = Category(name=iCAt)
        iceCreamCategory.save()
        iFav = request.POST.get("iceCreamFlavour")
        iceCreamFlavour = Flavour(flavour_name=iFav)
        iceCreamFlavour.save()
        iceCreamPriceBD = request.POST.get("IceCreamPrice")
        iceCreamPriceAD = request.POST.get("IceCreamPriceDec")
        iceCreamPrice = float(str(iceCreamPriceBD) + "." + str(iceCreamPriceAD))
        iceCreamDescSm = request.POST.get("IceCreamMiniDesc")
        iceCreamDescLg = request.POST.get("IceCreamLgDesc")
        iceCreamOrigin = request.POST.get("iceCreamCountry")
        iceCreamSeller = request.POST.get("iceCreamSellerName")
        iceCreamID = GenerateRandomId(iceCreamName, 5)
        ICECREAMs = AllProducts(
            products_id=iceCreamID,
            product_slug=iceCreamSlug,
            product_image=iceCreamImage,
            product_manufacturer=icecreamManufacture,
            product_name=iceCreamName,
            product_category=iceCreamCategory,
            product_flavour=iceCreamFlavour,
            product_price=iceCreamPrice,
            product_desc_sm=iceCreamDescSm,
            product_desc_lg=iceCreamDescLg,
            product_seller=iceCreamSeller,
            product_origin=iceCreamOrigin,
        )
        ICECREAMs.save()
        # Display a notification
        messages.success(request, "Ice Cream Uploaded To Our DataBase.")
        return redirect("uploadproducts")
    return render(request, "products/upload_product.html")


def current_Product(request, slug):
    cart_items = Cart.objects.filter(user=request.user)
    # fetching the product from via slug
    GotTheProduct = AllProducts.objects.filter(product_slug=slug).first()
    # getting the particular comments for "this" product
    comments = ProductComment.objects.filter(Productpost=GotTheProduct, parent=None)
    replies = ProductComment.objects.filter(Productpost=GotTheProduct).exclude(
        parent=None
    )
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    # setting similar icecreams
    SimilarProductCat = AllProducts.objects.filter(
        product_category__name=GotTheProduct.product_category.name
    ).exclude(product_slug=slug)[
        :2
    ]  # type: ignore
    SimilarProductFla = AllProducts.objects.filter(
        product_flavour__flavour_name=GotTheProduct.product_flavour.flavour_name
    ).exclude(product_slug=slug)[
        :2
    ]  # type: ignore

    # if slug doesn't match gives error
    if GotTheProduct is None:
        return render(request, "needs/404.html")

    # Comment Review System=================================================================================================

    likedcomments = CommentLike.objects.filter(useris=request.user)
    dislikedcomments = CommentDislike.objects.filter(useris=request.user)

    likedcomments = CommentLike.objects.filter(
        useris=request.user,
    )
    likes1 = {}
    for like in likedcomments:
        if like.commentIs.sno not in likes1.keys():
            likes1[like.commentIs.sno] = [like]
        else:
            likes1[like.commentIs.sno].append(like)

    dislikedcomments = CommentDislike.objects.filter(useris=request.user)
    dislikes1 = {}
    for like in dislikedcomments:
        if like.commentIs.sno not in dislikes1.keys():
            dislikes1[like.commentIs.sno] = [like]
        else:
            dislikes1[like.commentIs.sno].append(like)

    if request.method == "POST":
        do = request.POST.get("actionis")
        if do == "like":
            commentSno = request.POST.get("commentLike")
            ParentProductId = request.POST.get("prodictis")
            ParentProduct = AllProducts.objects.get(products_id=ParentProductId)
            commentTarget = ProductComment.objects.get(sno=commentSno)
            commentReviews = CommentLike.objects.filter(
                commentIs=commentTarget, useris=request.user
            ).first()
            # getting user which is liked the comment once
            reviewUserplus = CommentLike.objects.filter(
                useris=request.user, commentIs=commentTarget, liked=True
            ).first()

            if reviewUserplus is None:
                if commentReviews is None:
                    # Adding to liked comments
                    CommentLike.objects.create(
                        commentIs=commentTarget,
                        useris=request.user,
                        liked=True,
                        icon='<i class="bi bi-hand-thumbs-up-fill"></i>',
                    )
                    # Adding to disliked comments
                    CommentDislike.objects.create(
                        commentIs=commentTarget,
                        useris=request.user,
                        disliked=False,
                        icon='<i class="bi bi-hand-thumbs-down"></i>',
                    )
                else:
                    # Adding to liked comments
                    ins1 = CommentLike.objects.get(
                        commentIs=commentTarget, useris=request.user
                    )
                    ins1.liked = True
                    ins1.icon = '<i class="bi bi-hand-thumbs-up-fill"></i>'
                    ins1.save()
                    # Adding to disliked comments
                    ins2 = CommentDislike.objects.get(
                        commentIs=commentTarget, useris=request.user
                    )
                    ins2.disliked = False
                    ins2.icon = '<i class="bi bi-hand-thumbs-down"></i>'
                    ins2.save()

                # incrementing the like of the main comment
                commentTarget.Likes = commentTarget.Likes + 1
                if commentTarget.disLike != 0:
                    commentTarget.disLike = commentTarget.disLike - 1
                commentTarget.save()
                messages.success(request, "Comment Liked!!")
                return redirect(f"/stock/products/{ParentProduct.product_slug}")
            else:
                messages.error(request, "You Already Liked The Comment!!")
                return redirect(f"/stock/products/{ParentProduct.product_slug}")

        if do == "dislike":
            commentSno = request.POST.get("commentDislike")
            ParentProductId = request.POST.get("prodictis")
            ParentProduct = AllProducts.objects.get(products_id=ParentProductId)
            commentTarget = ProductComment.objects.get(sno=commentSno)
            commentReviews = CommentLike.objects.filter(
                commentIs=commentTarget, useris=request.user
            ).first()
            # getting user which is disliked the comment once
            reviewUserminus = CommentDislike.objects.filter(
                useris=request.user, commentIs=commentTarget, disliked=True
            ).first()

            if reviewUserminus is None:
                if commentReviews is None:
                    # Adding to liked comments
                    CommentLike.objects.create(
                        commentIs=commentTarget,
                        useris=request.user,
                        liked=False,
                        icon='<i class="bi bi-hand-thumbs-up"></i>',
                    )
                    # Adding to disliked comments
                    CommentDislike.objects.create(
                        commentIs=commentTarget,
                        useris=request.user,
                        disliked=True,
                        icon='<i class="bi bi-hand-thumbs-down-fill"></i>',
                    )
                else:
                    # Adding to liked comments
                    ins1 = CommentLike.objects.get(
                        commentIs=commentTarget, useris=request.user
                    )
                    ins1.liked = False
                    ins1.icon = '<i class="bi bi-hand-thumbs-up"></i>'
                    ins1.save()
                    # Adding to disliked comments
                    ins2 = CommentDislike.objects.get(
                        commentIs=commentTarget, useris=request.user
                    )
                    ins2.disliked = True
                    ins2.icon = '<i class="bi bi-hand-thumbs-down-fill"></i>'
                    ins2.save()

                # incrementing the like of the main comment
                commentTarget.disLike = commentTarget.disLike + 1
                if commentTarget.Likes != 0:
                    commentTarget.Likes = commentTarget.Likes - 1
                commentTarget.save()
                messages.success(request, "Comment Disiked!!")
                return redirect(f"/stock/products/{ParentProduct.product_slug}")
            else:
                messages.error(request, "You Already Disliked The Comment!!")
                return redirect(f"/stock/products/{ParentProduct.product_slug}")

    # End of comment review system==========================================================================================

    # otherwise render
    context = {
        "product": GotTheProduct,
        "similarIcecreamscat": SimilarProductCat,
        "similarIcecreamsfla": SimilarProductFla,
        "NoCartItems": cart_items,
        "comments": comments,
        "user": request.user,
        "likedComment": likes1,
        "dislikedComment": dislikes1,
        "replies": replyDict,
    }
    return render(request, "products/product.html", context)


def ipComment(request):
    if request.method == "POST":
        comment = request.POST.get("productComment")
        user = request.user
        product_identity = request.POST.get("product-identity-digit")
        postproduct = AllProducts.objects.get(products_id=product_identity)
        parentSno = request.POST.get("Comment_target_initilizer")

        # this section is for main product comments
        if parentSno == "":
            blogcomment = ProductComment(
                Productcomment=comment, user=user, Productpost=postproduct
            )
            blogcomment.save()
            # send a notification
            messages.success(request, "Comment Posted!!")

        # this section is for reply comments
        else:
            parentreply = request.POST.get("parentSno")
            replycomment = request.POST.get("replycomment")
            print(parentreply, replycomment)
            parent = ProductComment.objects.get(sno=parentreply)
            blogcomment = ProductComment(
                Productcomment=replycomment,
                user=user,
                Productpost=postproduct,
                parent=parent,
            )
            blogcomment.save()
            # send a notification
            messages.success(request, "Reply Posted Successfully!!")

    return redirect(f"/stock/products/{postproduct.product_slug}")  # type: ignore

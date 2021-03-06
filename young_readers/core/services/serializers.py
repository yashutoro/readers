from rest_framework import serializers
from .models import BookItems, BookItemsDtl, Subscriptions, Transactions, Wishlist
from core.authentication.serializers import UsersListSerializer

class BookItemsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookItemsDtl
        
        
class BookItemsSerializer(serializers.ModelSerializer):
    books = BookItemsDetailSerializer(many = True, read_only = True)
    
    class Meta:
        model = BookItems

class BookItemsListSerializer(serializers.ModelSerializer):
    
    book_status = serializers.SerializerMethodField('getBookStatus')

    def getBookStatus(self, obj):
        if self.context['request'].user.is_authenticated():
            user_id = self.context['request'].user.pk
            result = Transactions.objects.filter(book_id__ISBN_13 = obj.ISBN_13, action = 'requested', user_id = user_id)
            if len(result) > 0:
                return False
            else:
                return True
        else:
            return True

    class Meta:
        model = BookItems
        fields = ('book_id','ISBN_10','ISBN_13','title','author','item_type','cover_type','image','available_count','publisher','subject','total_count', 'book_status')
 
class BookItemsDtlSerializer(serializers.ModelSerializer):
    book_status = serializers.SerializerMethodField('getBookStatus')

    def getBookStatus(self, obj):
        user_id = self.context['request'].user.pk
        result = Transactions.objects.filter(book_id__ISBN_13 = obj.ISBN_13, action = 'requested', user_id = user_id)
        if len(result) > 0:
            return False
        else:
            return True


    class Meta:
        model = BookItems
        fields = ('ISBN_10','ISBN_13','title','author','item_type','cover_type','image','available_count','publisher','subject','total_count','book_status','description','pages')

class SubscriptionsSerializer(serializers.ModelSerializer):
    
    username = serializers.SerializerMethodField('getUsername')
    profile_pic = serializers.SerializerMethodField('getProfilePic')

    def getUsername(self, obj):
        return obj.user_id.username

    def getProfilePic(self, obj):
        return obj.user_id.profile_pic

    class Meta:
        model = Subscriptions
        
class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions

class TransactionsDtlSerializer(serializers.ModelSerializer):
    
    ISBN = serializers.SerializerMethodField('getISBN')
    title = serializers.SerializerMethodField('getTitle')
    author = serializers.SerializerMethodField('getAuthor')
    item_type = serializers.SerializerMethodField('getBookType')
    book_image = serializers.SerializerMethodField('getBookImage')

    def getISBN(self, obj):
        return obj.barcode_id.book_id.ISBN

    def getTitle(self, obj):
        return obj.barcode_id.book_id.title

    def getAuthor(self, obj):
        return obj.barcode_id.book_id.author

    def getBookType(self, obj):
        return obj.barcode_id.item_type

    def getBookImage(self, obj):
        return obj.barcode_id.book_id.image

    class Meta:
        model = Transactions
        fields = ('dof_request', 'ISBN', 'title', 'author', 'item_type', 'book_image')

class BookItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookItems
        fields = ('ISBN_10','ISBN_13','title','author','item_type','cover_type','image','available_count','publisher','subject','total_count')

class WishlistSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('getTitle')
    image = serializers.SerializerMethodField('getImage')
    cover_type = serializers.SerializerMethodField('getType')

    def getTitle(self, obj):
        return obj.book_id.title

    def getImage(self, obj):
        return obj.book_id.image

    def getType(self, obj):
        return obj.book_id.cover_type

    class Meta:
        model = Wishlist
        fields = ('id', 'user_id', 'book_id', 'audit_dttm', 'book_name', 'status', 'title', 'image', 'cover_type', 'quantity')

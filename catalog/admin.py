from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Registra el género de forma simple
admin.site.register(Genre)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # NUEVO: Añadimos 'borrower' a la lista que se ve en la tabla
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    
    # NUEVO: Filtros útiles para buscar libros rápidamente
    list_filter = ('status', 'due_back')
    
    # NUEVO: Organizamos las cajas de texto al editar una copia
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
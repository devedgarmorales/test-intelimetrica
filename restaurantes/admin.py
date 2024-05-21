from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
import csv
import uuid

# Register your models here.
from .models import Restaurante


class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sitio', 'telefono', 'clasificacion')

from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # HOME
    # =========================

    path(
        '',
        views.home,
        name='home'
    ),


    # =========================
    # AUTHENTICATION
    # =========================

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),


    # =========================
    # DASHBOARD
    # =========================

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    # =========================
    # CAREER RECOMMENDATION
    # =========================

    path(
        'recommendation/',
        views.recommendation,
        name='recommendation'
    ),


    # =========================
    # RECOMMENDATION HISTORY
    # =========================

    path(
        'history/',
        views.recommendation_history,
        name='history'
    ),


    # =========================
    # RECOMMENDATION DETAILS
    # =========================

    path(
        'history/<int:recommendation_id>/',
        views.recommendation_detail,
        name='recommendation_detail'
    ),


    # =========================
    # DELETE RECOMMENDATION
    # =========================

    path(
        'history/<int:recommendation_id>/delete/',
        views.delete_recommendation,
        name='delete_recommendation'
    ),
]
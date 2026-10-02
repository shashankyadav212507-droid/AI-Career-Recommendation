from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg

from .models import CareerProfile, CareerRecommendation
from ml.predictor import predict_career


# =========================================================
# HOME
# =========================================================

def home(request):
    return render(request, 'home.html')


# =========================================================
# REGISTER
# =========================================================

def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password:
            messages.error(
                request,
                'All fields are required.'
            )
            return redirect('register')

        if password != confirm_password:
            messages.error(
                request,
                'Passwords do not match.'
            )
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(
                request,
                'Username already exists.'
            )
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(
                request,
                'Email already registered.'
            )
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            'Registration successful! You can now login.'
        )

        return redirect('login')

    return render(request, 'register.html')


# =========================================================
# LOGIN
# =========================================================

def user_login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(
                request,
                'Username and password are required.'
            )
            return redirect('login')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f'Welcome back, {user.username}!'
            )

            return redirect('home')

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

            return redirect('login')

    return render(request, 'login.html')


# =========================================================
# LOGOUT
# =========================================================

def user_logout(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out successfully.'
    )

    return redirect('home')


# =========================================================
# DASHBOARD
# =========================================================

@login_required(login_url='login')
def dashboard(request):

    recommendations = CareerRecommendation.objects.filter(
        user=request.user
    ).order_by('-created_at')

    total_recommendations = recommendations.count()

    latest_recommendation = recommendations.first()

    average_confidence = recommendations.aggregate(
        average=Avg('confidence')
    )['average']

    if average_confidence is None:
        average_confidence = 0

    recent_recommendations = recommendations[:5]

    context = {
        'total_recommendations': total_recommendations,
        'latest_recommendation': latest_recommendation,
        'average_confidence': average_confidence,
        'recent_recommendations': recent_recommendations,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


# =========================================================
# CAREER RECOMMENDATION
# =========================================================

@login_required(login_url='login')
def recommendation(request):

    if request.method == 'POST':

        education = request.POST.get('education')

        programming_languages = request.POST.get(
            'programming_languages'
        )

        technical_skills = request.POST.get(
            'technical_skills'
        )

        interests = request.POST.get(
            'interests'
        )

        experience_level = request.POST.get(
            'experience_level'
        )

        preferred_domain = request.POST.get(
            'preferred_domain'
        )

        cgpa = request.POST.get(
            'cgpa'
        )

        problem_solving = request.POST.get(
            'problem_solving'
        )

        work_preference = request.POST.get(
            'work_preference'
        )

        work_type = request.POST.get(
            'work_type'
        )


        # =================================================
        # VALIDATION
        # =================================================

        if not all([
            education,
            programming_languages,
            technical_skills,
            interests,
            experience_level,
            preferred_domain,
            cgpa,
            problem_solving,
            work_preference,
            work_type
        ]):

            messages.error(
                request,
                'Please complete all fields.'
            )

            return redirect('recommendation')


        # =================================================
        # CGPA VALIDATION
        # =================================================

        try:

            cgpa_value = float(cgpa)

        except ValueError:

            messages.error(
                request,
                'Please enter a valid CGPA.'
            )

            return redirect('recommendation')


        if cgpa_value < 0 or cgpa_value > 10:

            messages.error(
                request,
                'CGPA must be between 0 and 10.'
            )

            return redirect('recommendation')


        # =================================================
        # ML INPUT DATA
        # =================================================

        ml_data = {

            "combined_text": (
                f"{programming_languages} "
                f"{technical_skills} "
                f"{interests}"
            ),

            "education": education,

            "experience_level": experience_level,

            "preferred_domain": preferred_domain,

            "cgpa": cgpa_value,

            "problem_solving": problem_solving,

            "work_preference": work_preference,

            "work_type": work_type
        }


        # =================================================
        # ML PREDICTION
        # =================================================

        prediction = predict_career(
            ml_data
        )

        career = prediction["career"]

        confidence = float(
            prediction["confidence"]
        )

        description = prediction["description"]

        skills = prediction["skills"]

        learn = prediction["learn"]

        roadmap = prediction["roadmap"]

        top_careers = prediction["top_careers"]


        # =================================================
        # CAREER SUMMARY
        # =================================================

        career_summary = (

            f"Based on your {education} education, "

            f"your knowledge of "
            f"{programming_languages}, "

            f"your technical skills in "
            f"{technical_skills}, "

            f"and your interest in "
            f"{interests}, "

            f"our Machine Learning model identified "

            f"{career} as your top career match. "

            f"Your current experience level is "

            f"{experience_level}, "

            f"with {problem_solving} "
            f"problem-solving ability. "

            f"You prefer the "
            f"{preferred_domain} domain, "

            f"with a focus on "
            f"{work_preference} work "

            f"and {work_type} opportunities."
        )


        # =================================================
        # SAVE CAREER PROFILE
        # =================================================

        CareerProfile.objects.create(

            user=request.user,

            education=education,

            programming_languages=
                programming_languages,

            technical_skills=
                technical_skills,

            interests=interests,

            experience_level=
                experience_level,

            preferred_domain=
                preferred_domain,

            cgpa=cgpa_value,

            problem_solving=
                problem_solving,

            work_preference=
                work_preference,

            work_type=
                work_type
        )


        # =================================================
        # SAVE RECOMMENDATION
        # =================================================

        CareerRecommendation.objects.create(

            user=request.user,

            career=career,

            confidence=confidence,

            top_careers=top_careers,

            career_summary=
                career_summary,

            description=description,

            skills=skills,

            learn=learn,

            roadmap=roadmap
        )


        # =================================================
        # RESULT PAGE
        # =================================================

        return render(

            request,

            'result.html',

            {

                "education":
                    education,

                "programming_languages":
                    programming_languages,

                "technical_skills":
                    technical_skills,

                "interests":
                    interests,

                "experience_level":
                    experience_level,

                "preferred_domain":
                    preferred_domain,

                "cgpa":
                    cgpa,

                "problem_solving":
                    problem_solving,

                "work_preference":
                    work_preference,

                "work_type":
                    work_type,

                "career":
                    career,

                "confidence":
                    confidence,

                "description":
                    description,

                "skills":
                    skills,

                "learn":
                    learn,

                "roadmap":
                    roadmap,

                "top_careers":
                    top_careers,

                "career_summary":
                    career_summary
            }
        )


    return render(
        request,
        'recommendation.html'
    )


# =========================================================
# RECOMMENDATION HISTORY
# =========================================================

@login_required(login_url='login')
def recommendation_history(request):

    recommendations = CareerRecommendation.objects.filter(

        user=request.user

    ).order_by('-created_at')

    return render(

        request,

        'history.html',

        {
            'recommendations':
                recommendations
        }
    )


# =========================================================
# RECOMMENDATION DETAIL
# =========================================================

@login_required(login_url='login')
def recommendation_detail(
    request,
    recommendation_id
):

    recommendation = get_object_or_404(

        CareerRecommendation,

        id=recommendation_id,

        user=request.user
    )

    return render(

        request,

        'result.html',

        {

            "career":
                recommendation.career,

            "confidence":
                recommendation.confidence,

            "top_careers":
                recommendation.top_careers,

            "career_summary":
                recommendation.career_summary,

            "description":
                recommendation.description,

            "skills":
                recommendation.skills,

            "learn":
                recommendation.learn,

            "roadmap":
                recommendation.roadmap,

            "education":
                "",

            "programming_languages":
                "",

            "technical_skills":
                "",

            "interests":
                "",

            "experience_level":
                "",

            "preferred_domain":
                "",

            "cgpa":
                "",

            "problem_solving":
                "",

            "work_preference":
                "",

            "work_type":
                ""
        }
    )


# =========================================================
# DELETE RECOMMENDATION
# =========================================================

@login_required(login_url='login')
def delete_recommendation(
    request,
    recommendation_id
):

    recommendation = get_object_or_404(

        CareerRecommendation,

        id=recommendation_id,

        user=request.user
    )

    if request.method == 'POST':

        recommendation.delete()

        messages.success(
            request,
            'Recommendation deleted successfully.'
        )

        return redirect('history')

    return redirect('history')
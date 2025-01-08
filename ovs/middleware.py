from django.shortcuts import redirect

class SessionValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is logged out and trying to access a protected page
        if not request.user.is_authenticated and request.path not in ['/','/loginform', '/logout']:
            return redirect('loginform')
        
        response = self.get_response(request)
        return response
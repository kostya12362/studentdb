from .settings import PORTAL_URL

def students_proc(request):
	return {'PORTAL_URL': request.get_full_path() }
def page_title(request):
    if request.resolver_match:
        view_name = request.resolver_match.view_name
        title = f"{view_name.capitalize()}"
    return {"title": title}

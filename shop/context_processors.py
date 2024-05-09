def page_title(request):
    title = ""
    if request.resolver_match:
        view_name = request.resolver_match.view_name
        title = view_name.split(":")[0].capitalize()
    return {"title": title}

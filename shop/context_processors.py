def page_title(request):
    """
    Add the page title for a page, based on the view name.
    Capotalize the first letter of the title. Clears ":" and takes the first
    part of the view name before.
    """
    title = ""
    if request.resolver_match:
        view_name = request.resolver_match.view_name
        title = view_name.split(":")[0].capitalize()
    return {"title": title}

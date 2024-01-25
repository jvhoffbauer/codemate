def get_object_or_404(queryset, *filter_args, **filter_kwargs) -> Model:
    try:
        return _get_object_or_404(queryset, *filter_args, **filter_kwargs)  # type: ignore
    except (TypeError, ValueError, ValidationError):
        raise Http404()
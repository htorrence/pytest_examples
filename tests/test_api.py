import responses


@responses.activate
def test_cat_api_404():
    responses.add(
        responses.GET,
        'https://cat.reactjsgirls.com/cats',
        json={'whoops, there are no cats!'},
        status=404,
    )


@responses.activate
def test_cat_api_200():
    responses.add(
        responses.GET,
        'https://cat.reactjsgirls.com/cat',
        json={'cats': ['cat1']},
        status=200,
    )

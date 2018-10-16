import responses


@responses.activate
def test_cat_api_404():
    responses.add(
        responses.GET,
        'https://cat.reactjsgirls.com/cat',
        json='whoops, there are no cats!',
        status=404,
    )


@responses.activate
def test_cat_api_200():
    responses.add(
        responses.GET,
        'https://cat.reactjsgirls.com/cat',
        json={'cat': 'http://cat.reactjsgirls.com/images/6eb156f97b04eadbdd60c72a3a5b75f1.jpg'},
        status=200,
    )

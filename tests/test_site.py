# def test_site_index(client, captured_templates):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert len(captured_templates) == 1
#     template, context = captured_templates[0]
#     assert template.name == "index.html"
#     assert response.headers["content-Type"] == "text/html; charset=utf-8"

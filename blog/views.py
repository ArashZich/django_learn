from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
	context = {
		"articles":[
			{	"title": "accusamus beatae ad facilis cum similique qui sunt",
				"img": "https://via.placeholder.com/200/92c952",
				"description": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

			},
			{	"title": "reprehenderit est deserunt velit ipsam",
				"img": "https://via.placeholder.com/200/771796",
				"description": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"

			},
			{	"title": "officia porro iure quia iusto qui ipsa ut modi",
				"img": "https://via.placeholder.com/200/24f355",
				"description": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"

			},
			{	"title": "culpa odio esse rerum omnis laboriosam voluptate repudiandae",
				"img": "https://via.placeholder.com/200/d32776",
				"description": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
			}
		]
	}
	return render(request, "blog/home.html", context)



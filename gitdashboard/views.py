from django.shortcuts import render
import requests
import pygal

print("-- views file --")

# Create your views here.

def homepage(request):
    print("-- view homepage --")

    url = "https://api.github.com/users/ssubu28/repos"
    response = requests.get(url)
    results = response.json()
    context = {
    }

    return render(request, 'homepage.html', context)



def allrepos(request): 
    print("-- all repos --")

    url = "https://api.github.com/users/ssubu28/repos"
    response = requests.get(url)
    results = response.json()

    context = {
        'repos': results
    }

    return render(request, "allrepos.html", context)



def reposchart(request): 
    print("-- repos chart --")

    url = "https://api.github.com/users/ssubu28/repos"
    response = requests.get(url)
    results = response.json()

    bar_chart = pygal.HorizontalBar(spacing=10, margin_top=20, x_title='Size', y_title='Repo Names')
    bar_chart.title = 'Repositories size chart'

    for repo_dict in results:
        bar_chart.add(repo_dict['name'], int(repo_dict['size']))

    chart_svg = bar_chart.render_data_uri()

    context = {
        'rendered_chart_svg': chart_svg,
    }

    return render(request, "reposchart.html", context)


# Creating ⬢ djangodashboard03... done
# https://djangodashboard03.herokuapp.com/ | https://git.heroku.com/djangodashboard03.git

def reposlang(request): 
    print("-- repos lang --")

    languages_dict = {}

    url = "https://api.github.com/users/ssubu28/repos"
    response = requests.get(url)
    results = response.json()

    pie_chart = pygal.Pie()
    pie_chart.title = 'Languages used'

    # Counting languages and adding into dictionary. Replace key = none
    for repo_dict in results:
        if repo_dict['language'] not in languages_dict.keys():
            languages_dict[repo_dict['language']] = 1
        else:
            languages_dict[repo_dict['language']] += 1

    languages_dict['No language'] = languages_dict[None]
    del languages_dict[None]


    # Adding values in a pie chart
    for language in languages_dict.keys():
        pie_chart.add(language, languages_dict[language])

    lang_chart_svg = pie_chart.render_data_uri()

    context = {
        'lang_chart': lang_chart_svg
    }

    return render(request, "reposlang.html", context) 
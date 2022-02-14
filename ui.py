from plotly.offline import iplot

genre_rating_year_df = genres_df.groupby(['movie_year', 'genre'], as_index=False)[['kp_rating', 'imdb_rating']].mean()

N = len(top_genres)

data = []
drop_menus = []

# конструируем все интересующие нас линии
for i in range(N):
    genre = top_genres[i]
    genre_df = genre_rating_year_df[genre_rating_year_df.genre == genre]

    trace_kp = go.Scatter(
        x=genre_df.movie_year,
        y=genre_df.kp_rating,
        mode='lines',
        name=genre + ' КиноПоиск',
        visible=(i == 0)
    )
    trace_imdb = go.Scatter(
        x=genre_df.movie_year,
        y=genre_df.imdb_rating,
        mode='lines',
        name=genre + ' IMDb',
        visible=(i == 0)
    )
    data.append(trace_kp)
    data.append(trace_imdb)

# создаем выпадающие меню
for i in range(N):
    drop_menus.append(
        dict(
            args=['visible', [False] * 2 * i + [True] * 2 + [False] * 2 * (N - 1 - i)],
            label=top_genres[i],
            method='restyle'
        )
    )

layout = go.Layout(
    title='Фильмы по жанрам',
    updatemenus=list([
        dict(
            x=-0.1,
            y=1,
            yanchor='top',
            buttons=drop_menus
        )
    ]),
)

fig = go.Figure(data=data, layout=layout)
iplot(fig)

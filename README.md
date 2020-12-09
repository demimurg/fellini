# FELLINI [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/madmaxeatfax/fellini/blob/master/model.ipynb)

This is a small research project to solve the problem of searching for movies by plot description, as well as just by queries in a free, natural form. The model always offers five options closest to the search query. It uses [kinopoisk-top-250](https://www.kinopoisk.ru/lists/top250/?tab=all) or [imdb-top-250](https://www.imdb.com/chart/top/) movies dataset (depends on language you choose)

# Examples🧐

| Request | Response |
| ------ | ------ |
| `"Фильмы про вторую мировую войну"` | [Иди и смотри][goandsee] [А зори здесь тихие][zori] [В бой идут одни старики][stariki] [Могила светлячков][svetlyachki] |
| `"Снято Квентином Тарантино"` | [Бешеные псы][psi] [Джанго освобожденный][django] [Криминальное чтиво][chtivo] |
| `"Фильм про то, как собака ждала своего хозяина"` | [Хатико: Самый верный друг][hatiko] |
| `"Проснись, Нео!"`, `"Красная таблетка или синяя?"`, `"Фильм про хакера с идеями солипсизма"` | [Матрица][matrix] |
| `"Фильм про чувака который прилетел с другой планеты но выглядел как обычный человек, у него очки еще красные были"` | [Планета Ка-Пэкс][kapec] |
| `"Мультик про робота, который сначала чистил мусор, а потом попал в космос и влюбился"` | [ВАЛЛ·И][valli] |
| `"Мультик про белку, не помню как назывался"` | [Ледниковый период][period] |
| `"Две собаки вместе едят спагетти"` | [Леди и бродяга(3)][lady] |
| `"Фильм по повести Булгакова"` | [Собачье сердце][sobach] |
| `"Трогательная мелодрама"` | [Привидение][privedenie] [Мужики!..][nuts] |
| `"Где снимался Мэл Гибсон"` | [Храброе сердце][serce] [Апокалипсис][apokalipsys] |

[//]: #
   [goandsee]: <https://www.kinopoisk.ru/film/42571>
   [zori]: <https://www.kinopoisk.ru/film/43395>
   [stariki]: <https://www.kinopoisk.ru/film/25108>
   [svetlyachki]: <https://www.kinopoisk.ru/film/8219>
   [psi]: <https://www.kinopoisk.ru/film/394>
   [django]: <https://www.kinopoisk.ru/film/586397>
   [chtivo]: <https://www.kinopoisk.ru/film/342>
   [hatiko]: <https://www.kinopoisk.ru/film/387556>
   [matrix]: <https://www.kinopoisk.ru/film/301>
   [kapec]: <https://www.kinopoisk.ru/film/723>
   [valli]: <https://www.kinopoisk.ru/film/279102>
   [period]: <https://www.kinopoisk.ru/film/707>
   [lady]: <https://www.kinopoisk.ru/film/8227>
   [sobach]: <https://www.kinopoisk.ru/film/77335>
   [privedenie]: <https://www.kinopoisk.ru/film/1991>
   [nuts]: <https://www.kinopoisk.ru/film/46745>
   [serce]: <https://www.kinopoisk.ru/film/399>
   [apokalipsys]: <https://www.kinopoisk.ru/film/160977>


# Let’s get ready to rumble!

- Open notebook in [google colab](https://colab.research.google.com/github/madmaxeatfax/fellini/blob/master/model.ipynb)
- Choose language for search (russian default)
- Run all cells - Cmd/Ctrl + F9, scroll down to the last
- Edit query and run - Cmd/Ctrl + Enter
- Repeat last step until you'll be satisfied👌

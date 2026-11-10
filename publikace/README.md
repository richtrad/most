# Vydání webu MOST

Větev `main` obsahuje celou badatelnu včetně modelů, fotografií a projektů Blenderu. Značka `verejny-original-grafit-20261110` uchovává původní veřejnou sekci z GRAFITu. Interaktivní městský atlas má [vlastní repozitář](https://github.com/richtrad/stary-most).

GitHub Pages publikuje větev `gh-pages` z kořenového adresáře. Z čistého checkoutu spusťte `python publikace/build.py CESTA_K_NOVEMU_PRAZDNEMU_ADRESARI`. Vznikne statický web pro cestu `/most/`. Obsah výstupního adresáře publikujte do větve `gh-pages` po odeslání zdrojového commitu do `main`.

Kvůli [limitu velikosti stránek](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) se největší modely a balíky čtou přímo z veřejného repozitáře ve stejné revizi. Při změně modelu se jeho URL při sestavení aktualizuje. Každá původní veřejná příloha má i nadále vlastní cestu v repozitáři.

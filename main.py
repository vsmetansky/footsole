def main():
    UPL = League('Ukrainian Premier League')
    Leagues.add(UPL)

if __name__ == "__main__":
    from .models.league import League
    from .models.leagues import Leagues
    main()

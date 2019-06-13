#constructs and returns list of 'display' pages (routes)
def get_display_pages():
    display_all_page = DataRoute(RouteBuilder()
                                 .set_path(crud_paths.get('show_all'))
                                 .set_menu([paths.get('back')])
                                 .set_data_type(League))
    display_one_page = DataRoute(RouteBuilder()
                                 .set_path(crud_paths.get('show_one'))
                                 .set_menu([paths.get('back')])
                                 .set_data_type(League))
    return [display_all_page, display_one_page]

#constructs and returns list of 'sub_crud' pages (routes)
def get_sub_crud_pages():
    add_team_page = CudRoute(RouteBuilder()
                             .set_path(crud_paths.get('add_team'))
                             .set_menu([crud_paths.get('save'), paths.get('back')])
                             .set_data_type(League))
    add_game_page = CudRoute(RouteBuilder()
                             .set_path(crud_paths.get('add_game'))
                             .set_menu([crud_paths.get('save'), paths.get('back')])
                             .set_data_type(League))
    return [add_game_page, add_team_page]

#constructs and returns list of 'crud' pages (routes)
def get_crud_pages():
    add_page = CudRoute(RouteBuilder()
                        .set_path(crud_paths.get('add'))
                        .set_menu([crud_paths.get('add_team'), crud_paths.get('add_game'), crud_paths.get('save'), paths.get('back')])
                        .set_data_type(League)
                        .set_children(get_sub_crud_pages()))
    rem_page = CudRoute(RouteBuilder()
                        .set_path(crud_paths.get('rem'))
                        .set_menu([crud_paths.get('save'), paths.get('back')])
                        .set_data_type(League))
    upd_page = CudRoute(RouteBuilder()
                        .set_path(crud_paths.get('upd'))
                        .set_menu([crud_paths.get('add_team'), crud_paths.get('add_game'), crud_paths.get('save'), paths.get('back')])
                        .set_data_type(League)
                        .set_children(get_sub_crud_pages()))
    return [add_page, rem_page, upd_page] + get_display_pages()

#constructs and returns list of 'auth' pages (routes)
def get_auth_pages():
    client_page = Route(RouteBuilder()
                        .set_path(main_paths.get('client'))
                        .set_menu([crud_paths.get('show_all'), crud_paths.get('show_one'), paths.get('back')])
                        .set_children(get_display_pages()))
    admin_page = Route(RouteBuilder()
                       .set_path(main_paths.get('admin'))
                       .set_menu([crud_paths.get('show_all'), crud_paths.get('show_one'), crud_paths.get('add'), crud_paths.get('rem'), crud_paths.get('upd'), paths.get('back')])
                       .set_children(get_crud_pages()))
    return [admin_page, client_page]


def main():
    main_page = Route(RouteBuilder()
                      .set_children(get_auth_pages())
                      .set_menu([main_paths.get('client'), main_paths.get('admin')]))
    app = App(main_page)
    app.start()


if __name__ == "__main__":
    from view.paths import main_paths, crud_paths, paths
    from models.league import League
    from controllers.controller import App, Route, DataRoute, CudRoute, RouteBuilder
    main()

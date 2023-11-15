from pages.base_page import BasePage


class Dashboard(BasePage)

    text_scouts_panel = "//h6[text()="Scouts Panel"]"
    main_page_button =  "//*[@aria-label="menu"]"

    main_page_span = "//*[text()="Main page"]"
    players_span = "//*[text()="Players"]"
    polski_span = "//*[text()="Polski"]"
    sign_out_span = "//*[text()="Sign out"]"

    logo_scouts_panel = "//*[@title="Logo Scouts Panel"]"
    contact_label = "//*[text()="Dev team contact"]"
    scotus_panel_paragraph = "//p[text()="Player, match and report management panel."]"
    text_shortcuts = "//h2[text()="Shortcuts"]"
    add_player_label = "//*[text()="Add player"]"

    text_activity = "//h2[text()="Activity"]"
    text_last_created_player = "//h6[text()="Last created player"]"
    text_last_updated_player = "//h6[text()="Last updated player"]"
    

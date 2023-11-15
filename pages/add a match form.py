from pages.base_page import BasePage


class Add_a_match_from(BasePage):

    submit_button= "//button[@aria-label="menu"]"
    submit_label= "//*[text()="Submit"]"

    clear_buttom = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]"
    clear_label = "//*[text()="Clear"]"

    title = "/*[@id="__next"]/div[1]/main/div[2]/form/div[1]"
    title_text = "//*[@id="__next"]/div[1]/main/div[2]/form/div[1]/div/span"

    match_at_home_label = "//*[text()="Match at home"]"
    match_out_home_label = "//*[text()="Match out home"]"

    match_fieldset = "//fieldset"
    date_text = "//*[text()="Date"]"
    error_paragraph = "//p[text()="Required"]"
    text_scouts_panel = "//h6[text()="Scouts Panel"]"

    league_grid = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[8]"
    time_played_grid = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]"
    number_grid = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]"
    web_math_grid = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]"








package config


var GIN_MODE = "DEBUG"
var GIN_PORT = ":8000"

var TEMPLATES_DIR = "templates/*"

var STATIC_FILES_URL = "/static"
var STATIC_FILES_DIRS = "./staticfiles"


type AppUrls struct {
    Login    string
    Register string
    Profile   string
    Home     string
    Manage string
}

var URLS = AppUrls{
    Home:      "/",
    Profile:  "/profile",
    Manage: "/manage",
    Login:     "/auth/login",
    Register:  "/auth/register",
}
class window
{
 …
};
class window_with_toolbar : virtual public window
{
 …
};
class window_with_menu : virtual public window
{
 …
};
class window_with_menu_and_toolbar : public window_with_menu,
 public window_with_toolbar
{
 …
};

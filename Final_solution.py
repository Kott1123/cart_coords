"""Cartesian Coordinates Printer

This script allows the user to modify the given dictionary which is gonna export
our data for box and display information which contains visualviewport and content
features.

This script also calculates and prints the (X,Y) of the boxes location to what the
user can see. Additionally prints the (X,Y) of the boxes location regardless of the
visibility.

This script does not require any modules to be imported.
"""


display_info = {
    "visualViewport": {
        "offsetX": 0,
        "offsetY": 0,
        "pageX": 0,
        "pageY": 663,
        "clientWidth": 1065,
        "clientHeight": 1920,
        "scale": 1
    },
    "contentSize": {
        "x": 0,
        "y": 0,
        "width": 1065,
        "height": 3678
    }
}


box_info = {
    "x": 240,
    "y": 2220,
    "height": 20,
    "width": 200}


class Rectangle():
    """ A class to represent Rectangle objects

    ...

    Attributes
    ----------
    x : int
        an integer which represents the top-left corner's x coordinate of the given rectangle
    y : int
        an integer which represents the top-left corner's y coordinate of the given rectangle
    width : int
        an integer which represents the width of the given rectangle
    height : int
        an integer which represents the height of the given rectangle
    top_left : tuple
        a tuple which contains the x,y of the top left rectangle's corner
    top_right : tuple
        a tuple which contains the x,y of the top right rectangle's corner
    bot_left : tuple
        a tuple which contains the x,y of the bot left rectangle's corner
    bot_right : tuple
        a tuple which contains the x,y of the bot right rectangle's corner
    corners : tuple
        a tuple which contains all rectangle corners

    Methods
    -------
    __init__
        Initialize the new object collecting information from display_info -> contentsize

    all_corners
        Returns a tuple which contains with the following order all content
        corners (top-left,top-right,bot-left,bot-right)

    """

    def __init__(self, x=display_info["contentSize"]["x"], y=display_info["contentSize"]["y"], width=display_info["contentSize"]["width"], height=display_info["contentSize"]["height"]):
        """
        Parameters
        ----------
        x : int
            an integer which represents the top-left corner's x coordinate of the given rectangle
        y : int
            an integer which represents the top-left corner's y coordinate of the given rectangle
        width : int
            an integer which represents the width of the given rectangle
        height : int
            an integer which represents the height of the given rectangle

        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def all_corners(self, x=display_info["contentSize"]["x"], y=display_info["contentSize"]["y"], width=display_info["contentSize"]["width"], height=display_info["contentSize"]["height"]):
        """Returns a tuple which contains all rectangle's corners

        Parameters
        ----------
        x : int
            an integer which represents the top-left corner's x coordinate of the given rectangle
        y : int
            an integer which represents the top-left corner's y coordinate of the given rectangle
        width : int
            an integer which represents the width of the given rectangle
        height : int
            an integer which represents the height of the given rectangle

        Raises
        ------
        NotImplementedError
            If width or height are zero means that we have no rectangle but a straight line
            or a point on the canvas
        """
        if self.width == 0 or self.height == 0:
            raise NotImplementedError("Lines and points have no corners!")

        self.top_left = self.x, self.y
        self.top_right = self.x + self.width, self.y
        self.bot_left = self.x, self.y + self.height
        self.bot_right = self.x + self.width, self.y + self.height
        corners = (self.top_left, self.top_right,
                   self.bot_left, self.bot_right)
        return corners


class Visual_Viewport():
    """A class which represents visualviewport objects

    ...

    Attributes
    ----------
    x : int
        an integer which represents the top-left corner's x coordinate of the given visualviewport
    y : int
        an integer which represents the top-left corner's y coordinate of the given visualviewport
    width : int
        an integer which represents the ClientWidth of the given visualviewport
    height : int
        an integer which represents the ClientHeight of the given visualviewport
    scroll_x : int
        an integer which represents the amount of  pixels the user scrolled on x-axis
    scroll_y : int
        an integer which represents the amount of pixels the user scrolled on y-axis
    scale : float
        a float which represents how much we zoom in or zoom out. It is a multiplier
        when its greater than 1 we zoom in when its lower than 1 we zoom out

    Methods
    -------
    __init__
        Initializes the new object by collecting information from display_info - > visualviewport.
    scroll(scroll_x=0,scroll_y=0)
        Handles scroll events which comes from the user. scroll_x and scroll_y are both 0 by default.
    zoom(scale=1)
        Handles zoom events which comes from the user. zoom is 1 by default.

    """

    def __init__(self, x=display_info["visualViewport"]["pageX"], y=display_info["visualViewport"]["pageY"], width=display_info["visualViewport"]["clientWidth"], height=display_info["visualViewport"]["clientHeight"]):
        """Parameters
        ----------
        x : int
            an integer which represents the top-left corner's x coordinate of the given visualviewport
        y : int
            an integer which represents the top-left corner's y coordinate of the given visualviewport
        width : int
            an integer which represents the width of the given visualviewport
        height : int
            an integer which represents the height of the given visualviewport
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def scroll(self, scroll_x=0, scroll_y=0):
        """Returns new information depending the users events
        on scrolling x or y axis.

        If the args scroll_x and scroll_y aren't passed in, the default
        values 0 are used.

        """
        pass

    def zoom(self, scale=1):
        """Returns new information depending the users events
        on zooming.

        If the argument scale isn't passed in, the default value 0
        is used.

        """
        pass


class Box(Rectangle):
    """A class which represents box objects. Box objects are items
    which are contained in the content.

    ...
    Attributes
    ----------
    x : int
        an integer which represents the top-left corner's x coordinate of the given box
    y : int
        an integer which represents the top-left corner's y coordinate of the given box
    width : int
        an integer which represents the width of the given box
    height : int
        an integer which represents the height of the given box
    visual_viewport_x : int
        an integer which represents the top-left corner's x of the visualviewport
    visual_viewport_y : int
        an integer which represents the top-left corner's y of the visualviewport
    top_left_corner : tuple
        a tuple which contains the top-left corner's (x,y) coordinates with visualviewport's
        top-left corner being the point of origin
    top_right_corner : tuple
        a tuple which contains the top-right corner's (x,y) coordinates with visualviewport's
        top-left corner being the point of origin
    bot_left_corner : tuple
        a tuple which contains the bot-left corner's (x,y) coordinates with visualviewport's
        top-left corner being the point of origin
    bot_right_corner : tuple
        a tuple which contains the bot-right corner's (x,y) coordinates with visualviewport's
        top-left corner being the point of origin
    corners : tuple
        a tuple which contains all boxes corners relatively to the visualviewport
    first_visible_corner : tuple
        a tuple which contains the first visible boxes corner in relation
        to the visualviewport

    Methods
    -------
    __init__
        Initializes the new object by collecting information from box_info.
    corners_relative_to_visualviewport
        Returns the boxes corners relative to the visualviewport's top-left
        corner.
    corner_visibility_check
        Prints the first visible boxes corner relative to the visualviewport.
    x_axis_scan
        Firstly checks if box scans visualviewport on x-axis and then
        prints the top left corner of the box partition which is visible.
    y_axis_scan
        Firstly checks if box scans visualviewport on y-axis and then
        prints the top left corner of the box partition which is visible.
    megabox_check
        Firstly checks if the visualviewport is fully contained in the box.
        Then prints the top left corner of the box.
    activation
        Activates all boxes check functions in order to eliminate the case.



    """

    def __init__(self, x=box_info["x"], y=box_info["y"], width=box_info["width"], height=box_info["height"]):
        """
        Parameters
        ----------
        x : int
            an integer which represents the top-left corner's x coordinate of the given box
        y : int
            an integer which represents the top-left corner's y coordinate of the given box
        width : int
            an integer which represents the width of the given box
        height : int
            an integer which represents the height of the given box


        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def corners_relative_to_visualviewport(self, visual_viewport_x=display_info["visualViewport"]["pageX"], visual_viewport_y=display_info["visualViewport"]["pageY"]):
        """
        Parameters
        ----------
        visual_viewport_x : int
            an integer which represents the top-left corner's x of the visualviewport
        visual_viewport_y : int
            an integer which represents the top-left corner's y of the visualviewport

        Returns
        -------
        tuple
            a tuple of all corners relatively to visualviewport. Visualviewport's top
            left corner is used as the point of origin


        """
        # We start creating each boxes corner starting from top-left. We get the initial coordinates and we subtract visualviewport's (x,y) from each corner's (x,y)
        self.top_left_corner = self.x - visual_viewport_x, self.y - visual_viewport_y
        self.top_right_corner = self.x + self.width - \
            visual_viewport_x, self.y - visual_viewport_y
        self.bot_left_corner = self.x - visual_viewport_x, self.y + \
            self.height - visual_viewport_y
        self.bot_right_corner = self.x + self.width - \
            visual_viewport_x, self.y + self.height - visual_viewport_y
        # at the end we save all boxes corners in a variable named corners for later use.
        self.corners = self.top_left_corner, self.top_right_corner, self.bot_left_corner, self.bot_right_corner
        return self.corners

    def corner_visibility_check(self, visual_viewport_width=display_info["visualViewport"]["clientWidth"], visual_viewport_height=display_info["visualViewport"]["clientHeight"]):
        """Prints the first visible boxes corner if that is included in
        visualviewport.

        Parameters
        ----------
        visual_viewport_width : int
            an integer which represents the visualviewport's width
        visual_viewport_height : int
            an integer which represents the visualviewport's height

        """
        # We initialize first_visible_corner to an empty tuple until we find the first visible corner.
        first_visible_corner = ()
        # Testing boxes corners if they are inside the visualviewport
        for corner in self.corners:
            # Corner visibility check
            if 0 <= corner[0] <= visual_viewport_width and 0 <= corner[1] <= visual_viewport_height:
                first_visible_corner = corner
                break
        # Testing the first_visible corner with every corner.
        # The following "if" tree handles the events where 1,2 or all 4 boxes corners are visible relative to our visualviewport.
        # Top left corner test. We return the coordinates as they are.
        if first_visible_corner == self.top_left_corner:
            print(self.top_left_corner[0], self.top_left_corner[1])
        # Top right corner test. We return the new top-left corner which isnt the initial top-left cause its located outside the x-axis boundaries of visualviewport.We return 0 on x coordinate.
        elif first_visible_corner == self.top_right_corner:
            print(0, self.top_right_corner[1])
        # Bot left corner test. We return the new top-left corner which isnt the initial top-left cause its located outside the y-axis boundaries of visualviewport.We return 0 on y coordinate.
        elif first_visible_corner == self.bot_left_corner:
            print(self.bot_left_corner[0], 0)
        # Bot right corner test. We return the new top-left corner which isnt the initial top-left cause its located outside the x-axis and y-axis boundaries of visualviewport. We return 0 on x,y coordinates.
        elif first_visible_corner == self.bot_right_corner:
            print(0, 0)

    def x_axis_scan(self, visual_viewport_width=display_info["visualViewport"]["clientWidth"], visual_viewport_height=display_info["visualViewport"]["clientHeight"]):
        """Checks if box contains visualviewport on y-axis. Then 
        calculates and prints the top-left visible corner.

        Parameters
        ----------
        visual_viewport_width : int
            an integer which represents the visualviewport's width
        visual_viewport_height : int
            an integer which represents the visualviewport's height

        """
        # We make sure that visualviewport is fully contained in the box relatively to y-axis.
        # Which means that boxes top-left and bot-right corners are the boundaries of visualviewport's top-left bot-right corners on y-axis.
        if self.top_left_corner[1] < 0 and self.bot_right_corner[1] > visual_viewport_height:
            # Second step we handle all possible events in scanning.
            # 1st case -> Left vertical boxes line outside visualviewport and the right vertical is inside.
            # 2nd case -> Right vertical boxes line outside visualviewport and the left vertical is inside.
            # 3rd case -> Right vertical boxes line and Left vertical are both inside the visualviewport.
            if 0 <= self.top_left_corner[0] <= visual_viewport_width or 0 <= self.bot_right_corner[0] <= visual_viewport_width:
                if self.top_left_corner[0] < 0:
                    print(0, 0)
                else:
                    print(self.top_left_corner[0], 0)

    def y_axis_scan(self, visual_viewport_width=display_info["visualViewport"]["clientWidth"], visual_viewport_height=display_info["visualViewport"]["clientHeight"]):
        """Checks if box contains visualviewport on x-axis. Then 
        calculates and prints the top-left visible corner.

        Parameters
        ----------
        visual_viewport_width : int
            an integer which represents the visualviewport's width
        visual_viewport_height : int
            an integer which represents the visualviewport's height

        """
        # We make sure that visualviewport is fully contained in the box relatively to x-axis.
        # Which means that boxes top-left and bot-right corners are the boundaries of visualviewport's top-left bot-right corners on x-axis.
        if self.top_left_corner[0] < 0 and self.bot_right_corner[0] > visual_viewport_width:
            # Second step we handle all possible events in scanning.
            # 1st case -> Top horizontal boxes line outside visualviewport and the bot horizontal is inside.
            # 2nd case -> Bot horizontal boxes line outside visualviewport and the top horizontal is inside.
            # 3rd case -> Top horizontal boxes line and bot horizontal are both inside the visualviewport.
            if 0 <= self.top_left_corner[1] <= visual_viewport_height or 0 <= self.bot_right_corner[1] <= visual_viewport_height:
                if self.top_left_corner[1] < 0:
                    print(0, 0)
                else:
                    print(0, self.top_left_corner[1])

    def megabox_check(self, visual_viewport_width=display_info["visualViewport"]["clientWidth"], visual_viewport_height=display_info["visualViewport"]["clientHeight"]):
        """Checks if visualviewport is fully-contained in the box. Then 
        calculates and prints the top-left visible corner.

        Parameters
        ----------
        visual_viewport_width : int
            an integer which represents the visualviewport's width
        visual_viewport_height : int
            an integer which represents the visualviewport's height

        """
        # In order to be a sub-box must be fully contained on x and y axis.
        if (self.top_left_corner[0] < 0 and self.top_left_corner[1] < 0) and (self.bot_right_corner[0] > visual_viewport_width and self.bot_right_corner[1] > visual_viewport_height):
            print(0, 0)

    def activation(self):
        """Activates all boxes check methods
        """
        self.corners_relative_to_visualviewport()
        self.corner_visibility_check()
        self.x_axis_scan()
        self.y_axis_scan()
        self.megabox_check()


# creating our objects
content = Rectangle()
visual_viewport = Visual_Viewport()
box = Box()


# Trigger box activation check
box.activation()
print(
    f"Boxes coordinates in relation to visualviewport regardless of visibility are {box.top_left_corner}")

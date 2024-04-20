### User Authentication

Start

|

|--- Display Welcome Message

|

|--- Prompt for Login or Signup

|       |

|       |--- If Login Selected:

|       |       |

|       |       |--- Execute Login Process

|       |

|       |--- If Signup Selected:

|               |

|               |--- Display Signup Options

|                       |

|                       |--- If Customer Signup Selected:

|                       |       |

|                       |       |--- Execute Customer Signup Process

|                       |

|                       |--- If Vendor Signup Selected:

|                       |       |

|                       |       |--- Execute Vendor Signup Process

|                       |

|                       |--- If Delivery Agent Signup Selected:

|                       |       |

|                       |       |--- Execute Delivery Agent Signup Process

|                       |

|                       |--- If Admin Signup Selected:

|                               |

|                               |--- Execute Admin Signup Process

|

|--- User Menu

|       |

|       |--- Display Menu Options Based on User Role

|               |

|               |--- If Customer:

|               |       |

|               |       |--- Execute Customer Commands

|               |

|               |--- If Vendor:

|               |       |

|               |       |--- Execute Vendor Commands

|               |

|               |--- If Delivery Agent:

|               |       |

|               |       |--- Execute Delivery Agent Commands

|               |

|               |--- If Admin:

|                       |

|                       |--- Execute Admin Commands

|

|--- End

### Delivery Agent Commands:

Start

|

|--- Personal Details

|       |

|       |--- Display personal information

|

|--- Availability

|       |

|       |--- Update availability status

|

|--- Area Servicing

|       |

|       |--- Update areas serviced

|

|--- Orders: Current

|       |

|       |--- Display current orders

|

|--- Orders: Past

|       |

|       |--- Display past orders

|

|--- Logout

|       |

|       |--- End

End

### Vendor Commands:

Start

|

|--- View Vendor Books

|       |

|       |--- Display books associated with the vendor

|

|--- Search

|       |

|       |--- Search for books based on criteria

|

|--- Add Book

|       |

|       |--- Add a new book to inventory

|

|--- Delete Book

|       |

|       |--- Remove a book from inventory

|

|--- Edit Book Stock

|       |

|       |--- Update stock quantity of a book

|

|--- Show Your Personal Details

|       |

|       |--- Display personal information of the vendor

|

|--- Logout

|       |

|       |--- End

End

### Customer Commands:

Start

|

|--- View Books

|       |

|       |--- Display available books

|

|--- Search

|       |

|       |--- Search for specific books

|

|--- Add Books to Cart

|       |

|       |--- Add books to shopping cart

|

|--- Show Order History

|       |

|       |--- Display order history

|

|--- Show Cart

|       |

|       |--- Display shopping cart contents

|

|--- Show Personal Details

|       |

|       |--- Display personal information

|

|--- Show Book Reviews

|       |

|       |--- View reviews for books

|

|--- Show DA Agent Reviews

|       |

|       |--- View reviews for delivery agents

|

|--- Place Order

|       |

|       |--- Proceed with placing order

|

|--- Clear Current Cart

|       |

|       |--- Clear shopping cart

|

|--- Know More About Any Book

|       |

|       |--- Display detailed book information

|

|--- Give Book Reviews

|       |

|       |--- Submit reviews for books

|

|--- Logout

|       |

|       |--- End

End

### Admin Commands:

Start

|

|--- Manage Pending Vendor Requests

|       |

|       |--- Approve/Disapprove Vendor

|               |

|               |--- Approve Vendor

|               |

|               |--- Disapprove Vendor

|

|--- Warehouse Management

|       |

|       |--- Add Warehouse

|       |

|       |--- Remove Warehouse

|       |

|       |--- Update Warehouse

|       |

|       |--- Show All the Warehouses

|

|--- Ban Management

|       |

|       |--- Ban Vendor/Customer

|               |

|               |--- Ban Vendor

|               |

|               |--- Ban Customer

|

|--- Unban Management

|       |

|       |--- Unban Vendor/Customer

|               |

|               |--- Unban Vendor

|               |

|               |--- Unban Customer

|

|--- Logout

|       |

|       |--- End

End
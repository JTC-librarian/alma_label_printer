# alma_label_printer
This Python script prints spine labels in Solent's required format. It takes a barcode as its input and pulls the call number from Alma via an API. It is designed for printing a single label at a time to a dedicated label printer. Solent use the Brother ptouch 2430 PC.
It could be useful to other institutions, but they will need to check - and probably edit - the parsing rules to suit their own requirements.
For the most part Solent use Spineomatic, which is an excellent piece of software. 
But as (a) library staff are increasingly restricted (no doubt for sound reasons) on what they can do on University computers, and (b) there is increasingly a need for updates to software to be packaged and pushed out rather than run as single updates (again for sound reasons), then it can be very time consuming to get a fix when an error with Spineomatic develops on a particular machine.
This script is useful as a stop-gap until the problems can be resolved.

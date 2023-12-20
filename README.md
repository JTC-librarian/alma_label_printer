# alma_label_printer
This Python script prints spine labels in Solent's required format. It takes a barcode as its input and pulls the call number from Alma via an API. It is designed for printing a single label at a time to a dedicated label printer. Solent use the Brother ptouch 2430 PC.
It could be useful to other institutions, but they will need to check - and probably edit - the parsing rules to suit their own requirements.
For the most part Solent use Spineomatic, which is an excellent piece of software. 
But as library staff are increasingly restricted (no doubt for sound reasons) on what they can do on University computers, and there is increasingly a need for updates to software to be packaged and pushed out (again for sound reasons), rather than run as single updates, it can be very time consuming when an error with Spineomatic develops on a particular machine.
This script is useful as a stop-gap until the problems can be resolved.

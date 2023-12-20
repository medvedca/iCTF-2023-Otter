# iCTF-2023-Otter
 
### DISCLAIMER: 
I was not a part of the challenge and started the serious attempt to solve it only after the CTF was over. 
The published solution was not satisfying for me, so I decided to write my own. I hope you will enjoy it. 
The publsihed solution involved a second image obtained from DALL-e website and I felt that it was not the 
intended solution. 

The suggested solution has not been beautified and, I am sure, it is not the most efficient one. Feel free 
to improve if you have time in your pocket :)  

### THE CHALLENGE:
You open your mailbox and find a strange postcard (invite.bmp). Flipping it around, you squint your eyes 
and try to decipher the wobbly handwriting:

MYSTERIOUS INVITE: 'On this most auspicious end of year, I otter invite you to my most magnanimous island party!'
YOU: 'This must be one of rich Jared's infamous parties, huh.'
MYSTERIOUS INVITE: 'Generative AI is all the rage this days, so I couldn't pass up the opportunity to use it 
for this year's invite. Have you heard models like Google's Imagen will include a hidden watermark on AI 
generated images? I might not have algorithms quite as fancy as Google's, but I've also encoded a little 
something into this invite--the address! Decode it, and you'll be more than welcome to attend.'
YOU: 'Who on Earth tells their guests to just figure out the address themselves?!'
MYSTERIOUS INVITE: 'One last piece of advice. All great thing come in three. Three sides to a triangle, 
three wise monkeys, three lights in a stoplight. Let the number three guide you, and you shall find my island.'
YOU: 'How is a stoplight a great thing? Sigh I can't say I understand the guy, but an island party is an 
island party. Let's get decoding, I guess.'

Objective: Determine the name of the island. The flag will be the name of the island enclosed by curly braces 
and prepended with ictf. Example: If the party were hosted in Happy Coconut Island, the flag would be 
ictf{Happy Coconut Island}

### DEPENDENCIES:

requirements.txt contains the list of required packages. The following comand line will install them:

> pip install -r requirements.txt

### RUNNING THE CODE:
> python3 decode-otter.py

If your python symlinked differently, change the command accordingly. 
The script will read input-otter-image.bmp image file that was provided by the organizers as the input
image decoding the island name. The script will produce the output image decoded-otter.bmp that contains 
readable coordinates of the island. The script will also launch an image viewer to display the output image. 

### METHOD:
The input image is 1024x1024 sRGB bitmap. The script creates histogram of pixel distribution by color 
separate for each channel. Then the script finds local minima and maxima in the histograms. The minima 
shows a very distinct pattern. To demonstrate it, the script outputs suppressed and pronounced colors
of the histogram. It looks like the encoder reassign colors for select pixels which happen to be an 
intersection of the original image and the encoded text. 

I am leaving figuring out the encoding algorithm to you to make it a bit more entertaining.

### AGHHH, THE ANSWER: 
... what do you see?

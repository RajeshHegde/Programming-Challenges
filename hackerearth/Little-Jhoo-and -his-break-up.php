<?php
/*
Little Jhool and his breakup:

After minting loads of money from innocent people by using the psychic powers (As we saw in the previous question!) - little Jhool managed to woo his girlfriend big Jhool! And now, he's in love - madly, madly in love with his girlfriend.

But the road to love is not easy as they say, little Jhool and big Jhool live in two different cities, and they often have to rely on multiple online clients to communicate. And many times, due to frustration, little Jhool starts hitting his keyboard, pressing the wrong keys - and thus, he ends up sending her a meaningless message, which frustrates his girlfriend - obviously. But big Jhool is a smart girl and she knows what to reciprocate back to her boyfriend's message based on the message she has received from him.

She figures that if and only if, she can delete several characters from the message sent by her boyfriend, resulting in the word "love", it will be considered that she managed to understand his message, and if not... well, some trouble is waiting for her boyfriend!

Input format:

There's only one line in the input, it contains the message sent by her boyfriend.

Output format:

If she managed to understand his message, print "I love you, too!" - else, print "Let us breakup!"

Constraints:

1 <= Length of message <= 100

Example:

Let's say that the message sent by him is: ahhellolvloe, the answer would be "I love you, too!" since it is possible that by deleting characters, she gets the word love.

Let's say that the message sent by him is: lvoe, the answer would be, "Let us breakup!" because there's no way you could get the word love by only using the delete operation.

PS: You can only perform deletion, on the message sent - you cannot rearrange the words in the message!

Sample Input (Plaintext Link)
lov3333333asdafajfgnkdfn33333e
Sample Output (Plaintext Link)
I love you, too!
Explanation
You can delete characters to get the word love.

*/
fscanf(STDIN, "%s\n", $message);
$length = strlen($message);
if ($length < 1 or $length > 100) {
	exit();
}
$love = false;
for ($i=0; $i < $length - 3 ; $i++) { 
	if($message[$i] == 'l'){
		for ($j=$i+1; $j < $length - 2; $j++) { 
			if($message[$j] == 'o'){
				for ($k=$j+1; $k < $length - 1; $k++) { 
					if ($message[$k] == 'v') {
						for ($l=$k+1; $l < $length; $l++) { 
							if ($message[$l] == 'e') {
								$love = true;
								break;
							}
						}
					}
					
				}
			}
		}

	}
}
if($love){
	echo "I love you, too!";
}
else{
	echo "Let us breakup!";
}
?>

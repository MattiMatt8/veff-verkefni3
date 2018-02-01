<!DOCTYPE html>
<html>
<head>
	<title>Liður 1</title>
</head>
<body>
<h2>Verkefni 3 <span style="font-size:18px;">Liður 1</span></h2>
%for manneskja in folk:
	{{manneskja[0]}} <a href="kt/{{manneskja[1]}}">{{manneskja[1]}}</a><br>
%end
<br><a href="/">Til baka</a>
</body>
</html>
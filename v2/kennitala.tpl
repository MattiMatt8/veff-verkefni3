<!DOCTYPE html>
<html>
<head>
	<title>Þversumma</title>
</head>
<body>
%þversumma = 0
%for tala in kt:
	%þversumma += int(tala)
%end
<h2>Þversumma</h2>
Þversumma kennitölunnar <strong>{{kt}}</strong> er <strong>{{þversumma}}</strong>
<br><br><a href="/1">Til baka</a>
</body>
</html>
%include('v2/header.tpl',titill = "Heim")
<div class="containerB">
	<div class="box">
		<h3>Túristar klifra yfir lokunarskilti</h3>
		<img src="myndir/lokad.png">
	</div>
	<div class="box">
		<h3>Bestu fréttirnar</h3>
		<ul>
		%for frett in frettir:
			<li><a href="frett/{{frett[1]}}">{{frett[0]}}</a></li>
		%end
			<br><a href="/">Til baka</a>
		</ul>
	</div>
</div>
%include('v2/footer.tpl')
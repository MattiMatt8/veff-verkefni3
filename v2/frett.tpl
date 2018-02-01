%include('v2/header.tpl', titill = "Frétt")
	<div class="containerB">
		<div class="box">
			<h3>{{titill}}</h3>
			<img src=/myndir/{{mynd}}>
		</div>
		<div class="box grein">
			<p>{{grein}}</p>
			<h5>{{netfang}}</h5>
			<a href="/2">Til baka</a>
		</div>
	</div>
%include('v2/footer.tpl')
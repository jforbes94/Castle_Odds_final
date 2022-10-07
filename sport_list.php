<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>

	</title>
</head>
<body>
	<table>
		<tr>
			<th>Game_ID</th>
			<th>Away_team</th>
			<th>O/U</th>
			<th>Moneyline</th>
		</tr>
		<?php
		$conn = mysqli_connect("CastleOdds.mysql.pythonanywhere-services.com","CastleOdds","banjobanjobanjo","CastleOdds$default")
		$sql = "SELECT * FROM games a ";
		$result = $conn->query($sql);

		if ($result->num_rows > 0) {
			while ($rows = $results-> fetch_assoc()) {
				echo "<tr><td>" . $row["home_team"]."</tr></td>". $row["away_team"]. "</tr></td>". $row["start_time"]. "</tr></td>".$row["sport_title"."</tr></td>"]
			}
		} else {
			echo "No Results";
		}
		$conn->close();
		?>
	</table>
</body>
</html>
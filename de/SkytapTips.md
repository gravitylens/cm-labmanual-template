## Verwenden von Skytap

Bevor Sie mit den Übungen beginnen, finden Sie hier einige Tipps, die Ihnen helfen, die Übungen effektiver zu meistern. Wenn Sie diese Tipps verstehen, wird das Laborerlebnis deutlich angenehmer.

Wenn Sie in der Laborumgebung ankommen, sind die Maschinen bereits in der richtigen Reihenfolge gestartet, um die Einhaltung der Dienstabhängigkeiten sicherzustellen. Möglicherweise stellen Sie fest, dass einige Maschinen noch nicht laufen. Dabei handelt es sich um selten genutzte, ressourcenintensive Maschinen. Die Anleitung weist Sie an, diese bei Bedarf zu starten.

::: pagebreak :::

### Herstellen einer Verbindung mit einer virtuellen Maschine

Klicken Sie auf das große Monitorsymbol, um eine Verbindung zu einer virtuellen Maschine mit dem HTML 5-Client herzustellen. Dadurch wird eine **Konsolenverbindung** zur virtuellen Maschine hergestellt.

![Großes Monitorsymbol](images/Skytap-Console-Connect.png)

::: Seitenumbruch :::

### Verwenden des Handbuchs auf kleinen Bildschirmen

Standardmäßig wird dieses Laborhandbuch als Panel rechts neben der virtuellen Maschine angezeigt. Dies funktioniert hervorragend auf größeren Bildschirmen, da Sie Labor und Anweisungen nebeneinander anzeigen können. Auf Bildschirmen, die nicht genügend Platz bieten, um alles gleichzeitig anzuzeigen, kann dies jedoch schwierig sein. Es gibt verschiedene Funktionen, die Ihnen dabei helfen.

#### Ändern der Größe der Hilfslinie

Sie können die Größe des rechten Bereichs verkleinern, um mehr Platz für die virtuelle Maschine zu schaffen.

![Leitfaden vergrößern oder verkleinern](images/Skytap-Resize-Guide.png)

Sollten die Bilder dadurch zu klein sein, klicken Sie auf das Bild, um es im Vollbildmodus anzuzeigen.

#### Den Leitfaden herausnehmen

**Öffnen Sie** den Guide, um ihn in einen anderen Browser-Tab oder sogar auf ein anderes Gerät zu verschieben.

![Skytap Popout](images/Skytap-Popout.png)

Anschließend können Sie das Laborhandbuch-Bedienfeld ausblenden und den gesamten verfügbaren Bildschirmplatz für die virtuelle Maschine freigeben.

::: Seitenumbruch :::

### Kopieren und Einfügen

Sie können zwischen einer virtuellen Maschine und Ihrer lokalen Maschine kopieren und einfügen. Skytap versucht dies, wenn Sie in einer virtuellen Maschine `ctrl-v` oder `ctrl-c` verwenden. Dies kann unzuverlässig sein, da es Probleme mit der Synchronisierung mit Ihrer lokalen Zwischenablage geben kann. Für bessere Ergebnisse verwenden Sie die Zwischenablage-Schaltfläche in der Skytap-Symbolleiste, um den Inhalt der Zwischenablage der virtuellen Maschine direkt zu bearbeiten. Wenn Sie innerhalb der virtuellen Maschine `right-click` kopieren und einfügen, wird nur versucht, die Zwischenablage der VM zu verwenden, um zuverlässigere Ergebnisse zu erzielen.

![Schaltfläche „Zwischenablage“](images/Skytap-Clipboard.png)

Es gibt auch Stellen mit ^^kopierbarem Text^^ in der Anleitung. Wenn Sie auf einen dieser ^^kopierbaren Texte^^ klicken, können Sie den Wert per `right-click` oder `ctrl-v` in die VM einfügen. Bitte haben Sie Geduld, da es normalerweise ein bis zwei Sekunden dauert, bis es funktioniert.

::: Seitenumbruch :::

### Tipps für maximale Produktivität

Verwenden Sie die Skytap-Symbolleiste auf jeder virtuellen Maschine, um Ihre Fähigkeit zur effizienten Interaktion mit dieser Maschine zu maximieren.

#### Vollbild

Das Vollbildsymbol passt die Größe Ihres virtuellen Bildschirms an die Bildschirmeinstellungen Ihres Computers an, um Scrollen zu vermeiden. Durch die Aktivierung des Vollbildmodus Ihres Browsers wird außerdem mehr Platz auf dem Bildschirm der virtuellen Maschine geschaffen und Ablenkungen werden minimiert.

![Vollbild-Schaltfläche](images/Skytap-Resize.png)

#### Bandbreiteneinstellungen

Bei langsameren Verbindungen müssen Sie möglicherweise Ihre Bandbreiteneinstellungen anpassen. Dadurch wird die Bildqualität der Verbindung reduziert, um Bandbreite zu sparen.

![Bandbreitentaste](images/Skytap-Bandwidth.png)

Skytap empfiehlt mindestens 1,2 Mbit/s Bandbreite pro laufender VM-Konsolensitzung. Latenz ist jedoch in der Regel die Hauptursache für schlechte Leistung.

#### STRG-ALT-ENTF

Verwenden Sie die Schaltfläche Strg-Alt-Entf in der Symbolleiste, um ein `Ctrl-Alt-Del` an die virtuelle Maschine zu senden.

![Strg-Alt-Entf-Taste](images/Skytap-C-A-D.png)

#### Verwenden von VPNs

Die Verbindung zu Skytap während einer VPN-Verbindung kann zu zusätzlicher Netzwerklatenz führen. Außerdem kann das GeoIP-Ortungssystem in Skytap dazu verleitet werden, Ihr Labor in einer Region bereitzustellen, die für Ihren Standort nicht ideal ist. Dies kann zu noch schwerwiegenderen Latenzproblemen führen. Vermeiden Sie VPN-Verbindungen, um die Reaktionsfähigkeit virtueller Maschinen zu verbessern.

::: pagebreak :::

### Globale Benutzer

Standardmäßig sind die Laborgeräte auf ein US-englisches Tastaturlayout eingestellt. Wenn Sie ein Gerät mit einem anderen Tastaturlayout verwenden, kann es zu ungewöhnlichem Verhalten Ihrer Laborgeräte kommen. Die Lösung besteht darin, das für Ihre Tastatur passende Tastaturlayout auf Ihren Laborgeräten zu installieren. Folgen Sie den nachstehenden Anweisungen, um das richtige Tastaturlayout für Ihre Tastatur zu finden und zu konfigurieren.

Gehen Sie im Startmenü zu Einstellungen &gt; Zeit und Sprache &gt; Sprache &gt; Sprache hinzufügen.

![Windows Sprache hinzufügen](images/Windows-Add-Language.png)

Wählen Sie Ihre Sprache aus. Klicken Sie auf Weiter. Sie können die Optionen für Sprache und Handschrift deaktivieren und dann auf Installieren klicken.

![Windows Sprache auswählen](images/Windows-Select-Language.png)

info&gt;Hinweis: Wenn Sie ein alternatives Tastaturlayout (z. B. AZERTY, Dvorak) verwenden, können Sie die Option neben Ihrer Sprache aktivieren, um diese zu installieren. Andernfalls schließen Sie das Fenster „Sprache“.

Klicken Sie in der Taskleiste auf „ENG“ und wählen Sie Ihr Tastaturlayout. Sie können zwischen den Tastaturlayouts wechseln. Ihr Dozent muss möglicherweise wieder auf ENG umschalten, um Ihnen bei den Übungen zu helfen. Deinstallieren Sie daher bitte keine Sprachoptionen.

![Windows-Sprache wechseln](images/Windows-Switch-Language.png)<br> <br>::: pagebreak :::

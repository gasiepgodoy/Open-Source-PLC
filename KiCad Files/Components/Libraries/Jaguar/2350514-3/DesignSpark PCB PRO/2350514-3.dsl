SamacSys ECAD Model
11296064/450068/2.50/3/4/Connector

DESIGNSPARK_INTERMEDIATE_ASCII

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "c217.5_h145"
		(holeDiam 1.45)
		(padShape (layerNumRef 1) (padShapeType Ellipse)  (shapeWidth 2.175) (shapeHeight 2.175))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 2.175) (shapeHeight 2.175))
	)
	(padStyleDef "s217.5_h145"
		(holeDiam 1.45)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 2.175) (shapeHeight 2.175))
		(padShape (layerNumRef 16) (padShapeType Rect)  (shapeWidth 2.175) (shapeHeight 2.175))
	)
	(textStyleDef "Default"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 50 mils)
			(strokeWidth 5 mils)
		)
	)
	(patternDef "SHDRRA3W90P0X350_1X3_1110X920X" (originalName "SHDRRA3W90P0X350_1X3_1110X920X")
		(multiLayer
			(pad (padNum 1) (padStyleRef s217.5_h145) (pt 0, 0) (rotation 90))
			(pad (padNum 2) (padStyleRef c217.5_h145) (pt 3.5, 0) (rotation 90))
			(pad (padNum 3) (padStyleRef c217.5_h145) (pt 7, 0) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Default") (isVisible True))
		)
		(layerContents (layerNumRef 30)
			(line (pt -2.6 -1.588) (pt 9.5 -1.588) (width 0.05))
		)
		(layerContents (layerNumRef 30)
			(line (pt 9.5 -1.588) (pt 9.5 11.25) (width 0.05))
		)
		(layerContents (layerNumRef 30)
			(line (pt 9.5 11.25) (pt -2.6 11.25) (width 0.05))
		)
		(layerContents (layerNumRef 30)
			(line (pt -2.6 11.25) (pt -2.6 -1.588) (width 0.05))
		)
		(layerContents (layerNumRef 28)
			(line (pt -2.35 1.5) (pt -2.35 11) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt -2.35 11) (pt 9.25 11) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt 9.25 11) (pt 9.25 1.5) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt 9.25 1.5) (pt -2.35 1.5) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt -2.35 0) (pt -2.35 11) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -2.35 11) (pt 9.25 11) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 9.25 11) (pt 9.25 1.5) (width 0.2))
		)
	)
	(symbolDef "2350514-3" (originalName "2350514-3")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 2) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 3) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(line (pt 200 mils 100 mils) (pt 600 mils 100 mils) (width 6 mils))
		(line (pt 600 mils 100 mils) (pt 600 mils -300 mils) (width 6 mils))
		(line (pt 600 mils -300 mils) (pt 200 mils -300 mils) (width 6 mils))
		(line (pt 200 mils -300 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 650 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Default"))

	)
	(compDef "2350514-3" (originalName "2350514-3") (compHeader (numPins 3) (numParts 1) (refDesPrefix J)
		)
		(compPin "1" (pinName "1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "2" (pinName "2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "3" (pinName "3") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "2350514-3"))
		(attachedPattern (patternNum 1) (patternName "SHDRRA3W90P0X350_1X3_1110X920X")
			(numPads 3)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
			)
		)
		(attr "Manufacturer_Name" "TE Connectivity")
		(attr "Manufacturer_Part_Number" "2350514-3")
		(attr "Mouser Part Number" "571-2350514-3")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/TE-Connectivity/2350514-3?qs=wnTfsH77Xs4%252BXocSlHm5VQ%3D%3D")
		(attr "Arrow Part Number" "2350514-3")
		(attr "Arrow Price/Stock" "https://www.arrow.com/en/products/2350514-3/te-connectivity?region=nac")
		(attr "Description" "2350514-3")
		(attr "Datasheet Link" "https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F2350514%7FA%7Fpdf%7FEnglish%7FENG_CD_2350514_A.pdf%7F2350514-3")
		(attr "Height" "6.91 mm")
	)

)

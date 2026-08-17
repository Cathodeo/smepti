' Gambas module file

'As the Github and Codeberg language detectors dont parse Gambas src files properly, adding this to be parsed'
'This is a copy of BattleUI.module on the /src directory'


Public Sub EncounterMsg(FoeId As Integer)

  Dim Msg As String
  Msg = "You encountered " & MainDB.GetCharname(FoeId)
  Textbox(Msg)

End


Public Sub ClearSect()

  Draw.FillRect(8, 160, 240, 64, 0)

End



Public Sub SelectUI()

ClearSect()
Draw.Rect(8, 160, 120, 64)
Draw.Text("1 - ATTACK", 24, 168)
Draw.Text("2 - E-SPELL", 24, 188)
Draw.Text("3 - DEFEND", 24, 208)

End

Public Sub SpellSelect()

  ClearSect()

  Draw.Rect(12, 160, 55, 64)
  Draw.Rect(71, 160, 55, 64)
  Draw.Rect(130, 160, 55, 64)
  Draw.Rect(189, 160, 55, 64)

End


Public Sub FoePortraitSingle(FoeId As Integer)

  Dim Path As String
  Dim img As Image
  Path = "images/foes/" & MainDB.GetCharname(FoeId) & ".png"
  img = Image.Load(Path)
  Draw.Image(img, 60, 10)



End



Public Sub Textbox(Text As String)

Dim Words As String[]
Dim Lines As String[]
Dim CurrentLine As String
Dim Word As String
Dim I As Integer



ClearSect()
Draw.Rect(8, 160, 240, 64)

Words = Split(Text, " ")
Lines = New String[]

For Each Word In Words

  If Len(CurrentLine) + Len(Word) + 1 > 30 Then
    Lines.Add(CurrentLine)
    CurrentLine = Word
  Else
    If CurrentLine = "" Then
      CurrentLine = Word
    Else
      CurrentLine &= " " & Word
    Endif
  Endif

Next

If CurrentLine <> "" Then Lines.Add(CurrentLine)

For I = 0 To Min(Lines.Count - 1, 2)
  Draw.Text(Str(Lines[I]), 20, 168 + (I * 20))
Next

End



 ' Gambas module file


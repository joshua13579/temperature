input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.temperature())
})
input.onSound(DetectedSound.Quiet, function () {
    music.play(music.createSoundExpression(WaveShape.Sine, 5000, 1, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
})

<template>
  <div class="container">
    <div class="col">
      <Grid :cols="3" :rows="2">
        <Key color="grey" code="0x01" name="SMART INSERT" />
        <Key color="grey" code="0x02" name="APPND" />
        <Key color="grey" code="0x03" name="RIPL O/WR" />
        <Key color="grey" code="0x04" name="CLOSE UP" />
        <Key color="grey" code="0x05" name="PLACE ON TOP" />
        <Key color="grey" code="0x06" name="SRC O/WR" />
      </Grid>
      <Grid :rows="4" :cols="3" :keysize="2">
        <Key color="white" name="IN" code="0x07" :width="1.5" />
        <Key color="white" name="OUT" code="0x08" :width="1.5" />
        <Key color="black" name="TRIM_IN" code="0x09" />
        <Key color="black" name="TRIM_OUT" code="0x0a" />
        <Key color="black" name="ROLL" code="0x0b" />
        <Key color="black" name="SLIP_SRC" code="0x0c" />
        <Key color="black" name="SLIP_DEST" code="0x0d" />
        <Key color="black" name="TRANS_DUR" code="0x0e" />
        <Key color="grey" name="CUT" code="0x0f" />
        <Key color="grey" name="DIS" code="0x10" />
        <Key color="grey" name="SMTH_CUT" code="0x11" />
      </Grid>
    </div>
    <div class="col">
      <Grid :cols="4" :rows="2">
        <Key color="grey" name="ESC" code="0x31" />
        <Key color="grey" name="SYNC_BIN" code="0x1f" />
        <Key color="black" name="AUDIO_LEVEL" code="0x2c" />
        <Key color="#eb4034" name="FULL_VIEW" code="0x2d" />
        <Key color="grey" name="TRANS" code="0x22" />
        <Key color="grey" name="SPLIT" code="0x2f" />
        <Key color="grey" name="SNAP" code="0x2e" />
        <Key color="grey" name="RIPL_DEL" code="0x2b" />
      </Grid>
      <Grid :cols="4" :rows="4">
        <Key color="black" name="CAM7" code="0x39" />
        <Key color="black" name="CAM8" code="0x3a" />
        <Key color="black" name="CAM9" code="0x3b" />
        <Key color="grey" name="LIVE_OWR" code="0x30" />
        <Key color="black" name="CAM4" code="0x36" />
        <Key color="black" name="CAM5" code="0x37" />
        <Key color="black" name="CAM6" code="0x38" />
        <Key color="grey" name="VIDEO_ONLY" code="0x25" />
        <Key color="black" name="CAM1" code="0x33" />
        <Key color="black" name="CAM2" code="0x34" />
        <Key color="black" name="CAM3" code="0x35" />
        <Key color="grey" name="AUDIO_ONLY" code="0x26" />
        <Key color="grey" name="STOP_PLAY" code="0x3c" :width="4" />
      </Grid>
    </div>
    <div class="col">
      <Grid :cols="3" :rows="1">
        <Key color="grey" name="SOURCE" code="0x1a" :width="1.5" />
        <Key color="grey" name="TIMELINE" code="0x1b" :width="1.5" />
      </Grid>
      <Grid :cols="3" :rows="1">
        <Key color="white" name="SHTL" code="0x1c" disabled="true" />
        <Key color="white" name="JOG" code="0x1d" disabled="true" />
        <Key color="white" name="SCRL" code="0x1e" disabled="true" />
      </Grid>
      <div class="circle">
        <Grid :cols="3" :rows="1">
          <Key color="black" name="WHEEL-LEFT" code="0xfe" :width="1.5" />
          <Key color="black" name="WHEEL-RIGHT" code="0xff" :width="1.5" />
        </Grid>
      </div>
    </div>
  </div>
</template>

<script setup>
useGatherAllBindings()
</script>

<style scoped>
.container {
  font-family: "Helvetica Neue", sans-serif;
  display: flex;
  gap: 20px;
  justify-content: center;
}
.col {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>

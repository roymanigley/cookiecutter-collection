class EagJellyfish extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({mode: 'open'});
        this.render();
    }

    render() {
        this.shadowRoot.innerHTML = `
      <style>
    .pixel {
        width: 8px;
        height: 8px;
        position: absolute;
    }

    .bell {
        box-shadow:
      /* Top row */
      32px 0px 0px #ff69b4,
      40px 0px 0px #ff69b4,
      48px 0px 0px #ff69b4,
      56px 0px 0px #ff69b4,

      /* Second row */
      24px 8px 0px #ff1493,
      32px 8px 0px #ff69b4,
      40px 8px 0px #ff69b4,
      48px 8px 0px #ff69b4,
      56px 8px 0px #ff69b4,
      64px 8px 0px #ff1493,

      /* Third row */
      16px 16px 0px #ff1493,
      24px 16px 0px #ff69b4,
      32px 16px 0px #ff69b4,
      40px 16px 0px #ff69b4,
      48px 16px 0px #ff69b4,
      56px 16px 0px #ff69b4,
      64px 16px 0px #ff69b4,
      72px 16px 0px #ff1493,

      /* Fourth row */
      8px 24px 0px #ff1493,
      16px 24px 0px #ff69b4,
      24px 24px 0px #ff69b4,
      32px 24px 0px #ff69b4,
      40px 24px 0px #ff69b4,
      48px 24px 0px #ff69b4,
      56px 24px 0px #ff69b4,
      64px 24px 0px #ff69b4,
      72px 24px 0px #ff69b4,
      80px 24px 0px #ff1493,

      /* Fifth row */
      8px 32px 0px #ff1493,
      16px 32px 0px #ff69b4,
      24px 32px 0px #ff69b4,
      32px 32px 0px #ff69b4,
      40px 32px 0px #ff69b4,
      48px 32px 0px #ff69b4,
      56px 32px 0px #ff69b4,
      64px 32px 0px #ff69b4,
      72px 32px 0px #ff69b4,
      80px 32px 0px #ff1493,

      /* Sixth row */
      8px 40px 0px #ff1493,
      16px 40px 0px #ff69b4,
      24px 40px 0px #ff69b4,
      32px 40px 0px #ff69b4,
      40px 40px 0px #ff69b4,
      48px 40px 0px #ff69b4,
      56px 40px 0px #ff69b4,
      64px 40px 0px #ff69b4,
      72px 40px 0px #ff69b4,
      80px 40px 0px #ff1493,

      /* Seventh row */
      16px 48px 0px #ff1493,
      24px 48px 0px #ff69b4,
      32px 48px 0px #ff69b4,
      40px 48px 0px #ff69b4,
      48px 48px 0px #ff69b4,
      56px 48px 0px #ff69b4,
      64px 48px 0px #ff69b4,
      72px 48px 0px #ff1493,

      /* Bottom row */
      24px 56px 0px #ff1493,
      32px 56px 0px #ff1493,
      40px 56px 0px #ff1493,
      48px 56px 0px #ff1493,
      56px 56px 0px #ff1493,
      64px 56px 0px #ff1493;
    }

    /* Jellyfish Tentacles */
    .tentacles {
        box-shadow:
      /* Left tentacle */
      20px 64px 0px #ff1493,
      20px 72px 0px #ff1493,
      16px 80px 0px #ff1493,
      16px 88px 0px #ff1493,
      20px 96px 0px #ff1493,
      20px 104px 0px #ff1493,

      /* Center-left tentacle */
      32px 64px 0px #ff1493,
      32px 72px 0px #ff1493,
      32px 80px 0px #ff1493,
      36px 88px 0px #ff1493,
      36px 96px 0px #ff1493,
      32px 104px 0px #ff1493,
      32px 112px 0px #ff1493,

      /* Center tentacle */
      44px 64px 0px #ff1493,
      44px 72px 0px #ff1493,
      44px 80px 0px #ff1493,
      44px 88px 0px #ff1493,
      40px 96px 0px #ff1493,
      40px 104px 0px #ff1493,
      44px 112px 0px #ff1493,
      44px 120px 0px #ff1493,

      /* Center-right tentacle */
      56px 64px 0px #ff1493,
      56px 72px 0px #ff1493,
      56px 80px 0px #ff1493,
      52px 88px 0px #ff1493,
      52px 96px 0px #ff1493,
      56px 104px 0px #ff1493,
      56px 112px 0px #ff1493,

      /* Right tentacle */
      68px 64px 0px #ff1493,
      68px 72px 0px #ff1493,
      72px 80px 0px #ff1493,
      72px 88px 0px #ff1493,
      68px 96px 0px #ff1493,
      68px 104px 0px #ff1493;
    }

    /* Eyes */
    .eyes {
        box-shadow:
      /* Left eye */
      28px 28px 0px #000,
      32px 28px 0px #000,
      28px 32px 0px #000,
      32px 32px 0px #000,

      /* Right eye */
      52px 28px 0px #000,
      56px 28px 0px #000,
      52px 32px 0px #000,
      56px 32px 0px #000;
    }

    .glow {
        box-shadow:
      32px 0px 0px 0px rgba(255, 105, 180, 0.3),
      40px 0px 0px 0px rgba(255, 105, 180, 0.3),
      48px 0px 0px 0px rgba(255, 105, 180, 0.3),
      56px 0px 0px 0px rgba(255, 105, 180, 0.3);
        filter: blur(1px);
    }

    .jelly-fish {
        position: relative;
        animation: float 4s ease-in-out infinite;
        padding: 2em;
        display: inline-block;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
      </style>

      <div class="jelly-fish">
    <div class="pixel bell"></div>
    <div class="pixel tentacles"></div>
    <div class="pixel eyes"></div>
    <div class="pixel glow"></div>
      </div>
  `;
    }
}

customElements.define('eag-jellyfish', EagJellyfish);
 
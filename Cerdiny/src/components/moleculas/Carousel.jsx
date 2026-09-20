import {
  EffectCards,
  Navigation,
  Pagination,
  Scrollbar,
  A11y,
  Autoplay,
} from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";
import "swiper/css/scrollbar";
import "swiper/css/effect-cards";
import img1 from "../../assets/Ruleta/ruleta9.png";
import img2 from "../../assets/Ruleta/ruleta8.png";
import img3 from "../../assets/Ruleta/ruleta5.png";
import img4 from "../../assets/Ruleta/ruleta6.png";
import img5 from "../../assets/Ruleta/ruleta7.png";

export function Carousel() {
  return (
    <div className="home-carousel">
      <Swiper
        autoplay={{ delay: 1500, disableOnInteraction: false }}
        modules={[
          EffectCards,
          Navigation,
          Pagination,
          Scrollbar,
          A11y,
          Autoplay,
        ]}
        navigation={true}
        pagination={{ type: "fraction" }}
        scrollbar={{ draggable: true }}
        effect="cards"
      >
        <SwiperSlide>
          <img src={img1} alt="Ruleta 1" />
        </SwiperSlide>
        <SwiperSlide>
          <img src={img2} alt="Ruleta 2" />
        </SwiperSlide>
        <SwiperSlide>
          <img src={img3} alt="Ruleta 3" />
        </SwiperSlide>
        <SwiperSlide>
          <img src={img4} alt="Ruleta 4" />
        </SwiperSlide>
        <SwiperSlide>
          <img src={img5} alt="Ruleta 5" />
        </SwiperSlide>
      </Swiper>
    </div>
  );
}
